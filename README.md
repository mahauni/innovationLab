# isso é o arquivo principal do innovation lab

Made in pyton 3.9.13
 
 Para fazer o aplicativo funcionar, você precisa do app IP Webcam
 Possivel instalar com a app store, tem nela
 Se houver outras possibilidades, estou de ouvidos abertos
 E na constante URL, mudar para a sua url do dispositivo
 
 To make the script work, you will need the app IP Webcam
 Possible to install it in the app store, it has in it
 If there are other possibles apps and ways to do the save image thing, Im all ears
 And in the constant URL, you will need to put your device url to make it work

How to start with this repo
===========================

Install all dependencies with: 
```bash
$ pip install -r requirements.txt
```

After the installation create a .env file with:
```bash
URL=YOUR_URL_FROM_OPENCV
```

And run your app with:
```bash
$ python3 app.py
```

# TODO:

- Colocar todas as informações no dynamo
- Arrumar um jeito de tentar pegar os ids das fotos uplodadas
- tentar fazer um modo separado para que seja possivel nós comandamos de fomra mais facil.
