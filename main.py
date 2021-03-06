# Usar OpenCv para utilizar a camera do celular e tirar fotos
import cv2
import numpy as np
import os
import requests
import imutils
import threading
import time
#import urllib.request

# URL from the IP webcam
URL = "http://192.168.0.15:8080/shot.jpg"
 
#not tested this version, only with the non alteration one. (the commented one)
def main():
    #create the directory images
    if not os.path.exists("images"):
        os.mkdir("images")

    # Começa a thread que vai fazer as fotos serem tiradas
    x = threading.Thread(target=thread_function, args=(2,), daemon=True)
    x.start()
    x.join()

    # Photos done and in the images dir
    print("Done!")
    print("After the process of virtualization.")
    input("Type enter to continue the process!")
    
    # Cosmetics selection
    inp = input("Want to add hair? (Y) (N)")
    if (inp.upper() == "Y"):
        hair = int(input("Which type of hair do you like (1) (2) (3) (4)"))
        Hair(hair)

    inp = input("Want to add accessories? (Y) (N)")
    if (inp.upper() == "Y"):
        accessories = int(input("Which type of hair do you like (1) (2) (3) (4)"))
        Accessories(accessories)
    
    #input("Type enter to continue the process!")

    # It makes the pose to take the photo
    os.system("start ./DAZ3D_Scripts/poseTest.duf")
    input("Type enter to continue the process!")

    # Takes the photo of the character
    os.system("start ./DAZ3D_Scripts/takePhoto.dsa")
## Find a way to know when the file is done and stop when its not done

    ## after this point is make a func to send the image 3d to the customer input (email for example)


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
    for j in range(0, i):
        pic = getImage(URL)
        cv2.imwrite("./images/pic"+str(j)+".jpg", pic)
        sharpen_photo(0)
        print("photo "+str(j)+" taken")
        time.sleep(1)

def sharpen_photo(j):
    image = cv2.imread("./images/pic"+str(j)+".jpg")
    sharpen_kernel = np.array([[-1,-1,-1], [-1,9,-1], [-1,-1,-1]])
    sharpen = cv2.filter2D(image, -1, sharpen_kernel)
    cv2.imwrite("./images/sharpenPic"+str(j)+".jpg", sharpen)
    
def Hair(x):
    if x == 1:
        os.system("start ./DAZ3D_Scripts/HairSelect/Armani Hair.duf")
    elif x == 2:
        os.system("start ./DAZ3D_Scripts/HairSelect/Armani Hair.duf")
    elif x == 3:
        os.system("start ./DAZ3D_Scripts/HairSelect/Armani Hair.duf")
    elif x == 4:
        os.system("start ./DAZ3D_Scripts/HairSelect/Armani Hair.duf")

def Accessories(x):
    if x == 1:
        os.system("start ./DAZ3D_Scripts/HairSelect/Armani Hair.duf")
    elif x == 2:
        os.system("start ./DAZ3D_Scripts/HairSelect/Armani Hair.duf")
    elif x == 3:
        os.system("start ./DAZ3D_Scripts/HairSelect/Armani Hair.duf")
    elif x == 4:
        os.system("start ./DAZ3D_Scripts/HairSelect/Armani Hair.duf")    

# Main
if __name__ == "__main__":
    main()