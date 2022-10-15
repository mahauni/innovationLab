# Usar OpenCv para utilizar a camera do celular e tirar fotos
import cv2
import numpy as np
import os
import requests
import imutils
import threading
import time
from tabulate import tabulate
import ast
from dotenv import dotenv_values
import boto3
from boto3.session import Session
from botocore.exceptions import NoCredentialsError
#import urllib.request

# URL from the IP webcam
global URL
config = dotenv_values("./.env") 
URL = config['URL']
ACCESS_KEY = config['ACCESS_KEY']
SECRET_KEY = config['SECRET_KEY']

def dbWrite(name, sex, hair, accessories, email):
    with open('./tables/listTable.txt', 'r') as f:
        file_contents = f.read()
        lista = ast.literal_eval(file_contents)


    user = [lista[len(lista)-1][0] + 1, name, sex.upper(), hair, accessories, 'pic'+ str(lista[len(lista)-1][0] + 1) +'.jpg', email]

    # Add the user
    lista.append(user)

    db = boto3.resource('dynamodb', region_name='us-east-1',  aws_access_key_id=ACCESS_KEY, aws_secret_access_key=SECRET_KEY)
    table = db.Table("avataringDb")

    table.put_item(
        Item={
        "email": email,
        "acessorio": str(accessories),
        "cabelo": str(hair),
        "idImagem": email +'.jpg',
        "nome": name,
        "sexo": sex
        }
    )

    # Write the user in the more table like file
    with open('./tables/table.txt', 'w') as fi:
        fi.write(tabulate(lista, headers='firstrow', tablefmt='fancy_grid'))

    # Write the list for the next user
    with open('./tables/listTable.txt', 'w') as fil:
        fil.write(str(lista))

def takePhoto(x):
    x = threading.Thread(target=thread_function, args=(x,), daemon=True)
    x.start()
    x.join()

# função de pegar a imagem pelo app
def getImage(url):
    img_resp = requests.get(url)
    img_arr = np.array(bytearray(img_resp.content), dtype = np.uint8)
    img = cv2.imdecode(img_arr, -1)
    img = imutils.resize(img, width=600, height=1200)
    return img

# essa é a função da thread, que é rodar independemente do main 
# para salvar as fotos em outro local
def thread_function(i):
    with open('./tables/listTable.txt', 'r') as f:
        file_contents = f.read()
        lista = ast.literal_eval(file_contents)

    for j in range(0, i):
        pic = getImage(URL)
        cv2.imwrite("./images/pic"+str(lista[len(lista)-1][0] + 1)+".jpg", pic)
        cv2.imwrite("./static/IMG/image.jpg", pic)
        # sharpen_photo(0)
        print("photo "+str(j)+" taken")
        time.sleep(1)

def sharpen_photo(j):
    image = cv2.imread("./images/pic"+str(j)+".jpg")
    sharpen_kernel = np.array([[-1,-1,-1], [-1,9,-1], [-1,-1,-1]])
    sharpen = cv2.filter2D(image, -1, sharpen_kernel)
    cv2.imwrite("./images/sharpenPic"+str(j)+".jpg", sharpen)

def downloadS3(bucket, path):
    # session = Session(aws_access_key_id=ACCESS_KEY,
    #             aws_secret_access_key=SECRET_KEY)
    # s3 = session.resource('s3')
    # your_bucket = s3.Bucket(bucket)

    # for s3_file in your_bucket.objects.all():
    #     print(s3_file.key) # prints the contents of bucket
    s3 = boto3.client('s3', aws_access_key_id=ACCESS_KEY,
                      aws_secret_access_key=SECRET_KEY)

    # get last updated photo which is the photo we just took
    get_last_modified = lambda obj: int(obj['LastModified'].strftime('%s'))

    objs = s3.list_objects_v2(Bucket='avataring-img')['Contents']
    last_added = [obj['Key'] for obj in sorted(objs, key=get_last_modified)][-1]
    s3.download_file(bucket, last_added, path)

    # another way to get the file with the name you put in the aws
    # s3.download_file(bucket, name, path)

def downloadSpecificS3(bucket, filename, path):
    s3 = boto3.client('s3', aws_access_key_id=ACCESS_KEY,
                      aws_secret_access_key=SECRET_KEY)

    try:
        s3.download_file(bucket, filename, path)
        return "OK"
    except:
        return None


def uploadToS3(local_file, bucket, s3_file):
    s3 = boto3.client('s3', aws_access_key_id=ACCESS_KEY,
                      aws_secret_access_key=SECRET_KEY)

    try:
        s3.upload_file(local_file, bucket, s3_file)
        print("Upload Successful")
        return True
    except FileNotFoundError:
        print("The file was not found")
        return False
    except NoCredentialsError:
        print("Credentials not available")
        return False

def main():
    print("start")

# Main if you want to run this file alone
if __name__ == "__main__":
    main()
    # takePhoto(1)

    # # Photos done and in the images dir
    # print("Done!")
    # print("After the process of virtualization.")
    # input("Type enter to continue the process!")

    # name = input("Type your name: ")

    # email = input("Type your email: ")

    # sex = input("Which sex are you? (M) (F): ")

    # # Cosmetics selection
    # inp = input("Want to add hair? (Y) (N): ")
    # if (inp.upper() == "Y"):
    #     hair = int(input("Which type of hair do you like (1) (2) (3) (4): "))
    #     # Hair(hair)

    # inp = input("Want to add accessories? (Y) (N): ")
    # if (inp.upper() == "Y"):
    #     accessories = int(input("Which type of hair do you like (1) (2) (3) (4): "))

    # dbWrite(name, sex, hair, accessories, email)
