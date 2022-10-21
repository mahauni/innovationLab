import boto3
from botocore.exceptions import NoCredentialsError
from dotenv import dotenv_values
from tabulate import tabulate

config = dotenv_values("./.env") 
ACCESS_KEY = config['ACCESS_KEY']
SECRET_KEY = config['SECRET_KEY']

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

def dowloadFromDynamo():
    db = boto3.resource('dynamodb', region_name='us-east-1',  aws_access_key_id=ACCESS_KEY, aws_secret_access_key=SECRET_KEY)
    table = db.Table("avataringDb")

    response = table.scan()
    data = response['Items']

    while 'LastEvaluatedKey' in response:
        response = table.scan(ExclusiveStartKey=response['LastEvaluatedKey'])
        data.extend(response['Items'])

    with open('./tableTest.txt', 'w') as fi:
        fi.write(tabulate(data, headers='firstrow', tablefmt='fancy_grid'))

    # Write the list for the next user
    with open('./listTest.txt', 'w') as fil:
        fil.write(str(data))
        

def downloadSpecificS3(bucket, filename, path):
    s3 = boto3.client('s3', aws_access_key_id=ACCESS_KEY,
                      aws_secret_access_key=SECRET_KEY)

    try:
        s3.download_file(bucket, filename, path)
        return "OK"
    except:
        return None

def main():
    dowloadFromDynamo()

if __name__ == "__main__":
    main()

