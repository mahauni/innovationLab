# Usar OpenCv para utilizar a camera do celular e tirar fotos
import cv2
import numpy as np
import os
import requests
import imutils
import threading
import time
#import urllib.request

#url from the IP webcam
#URL = "http://192.168.0.15:8080/shot.jpg"

# função de pegar a imagem pelo app
def getImage(url):
    img_resp = requests.get(url)
    img_arr = np.array(bytearray(img_resp.content), dtype = np.uint8)
    img = cv2.imdecode(img_arr, -1)
    img = imutils.resize(img, width=1000, height=1800)
    return img

# essa é a função da thread, que é rodar independemente do main 
# para salvar as fotos em outro local
def thread_function(i):
    for j in range(0, i):
        pic = getImage("http://192.168.0.15:8080/shot.jpg")
        cv2.imwrite("./images/pic"+str(j)+".jpg", pic)
        time.sleep(1)

#not tested this version, only with the non alteration one. (the commented one)
def main():
    #create the directory images
    if not os.path.exists("images"):
        os.mkdir("images")

    # Começa a thread que vai fazer as fotos serem tiradas
    x = threading.Thread(target=thread_function, args=(5,), daemon=True)
    x.start()
    x.join()

# Main
if __name__ == "__main__":
    main()