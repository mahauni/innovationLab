# Usar OpenCv para utilizar a camera do celular e tirar fotos
import cv2
import numpy as np
import os
import requests
import imutils
#import urllib.request


#not tested this version, only with the non alteration one. (the commented one)
def main():
    #url from the IP webcam
    url = "http://192.168.0.15:8080/shot.jpg"

    #Save image with resolution alterations with it (didn't test it yet)
    #can delete this part if want to save the image from url
    img_resp = requests.get(url)
    img_arr = np.array(bytearray(img_resp.content), dtype = np.uint8)
    img = cv2.imdecode(img_arr, -1)
    img = imutils.resize(img, width=1000, height=1800)

    #create the directory images
    if not os.path.exists("images"):
        os.mkdir("images")

    #Need to test if will make it work
    savePhoto(img)

    #The full command tested and worked
    #print(cv2.imwrite("C:/LucasRaoni/fontes/workspace/python/innovation/images/pic1.jpg", img))
    
    #Save image directly from the url
    #print(urllib.request.urlretrieve(url, "C:/LucasRaoni/fontes/workspace/python/innovation/images/pic1.jpg"))

if __name__ == "__main__":
    main()

def savePhoto(pic):
    cv2.imwrite("./images/pic1.jpg", pic)