from flask import Flask, render_template, url_for, request, redirect
import os
import funcs
import ast

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = os.path.join('static', 'IMG')

@app.route('/form')
def index():
    PathHair1 = os.path.join(app.config['UPLOAD_FOLDER'], 'ArmaniHair.png')
    PathHair2 = os.path.join(app.config['UPLOAD_FOLDER'], 'BasicHair.png')
    PathHair3 = os.path.join(app.config['UPLOAD_FOLDER'], 'LaurenHair.duf.png')
    PathHair4 = os.path.join(app.config['UPLOAD_FOLDER'], 'ToulouseGenesis2Female.png')
    PathAcc1 = os.path.join(app.config['UPLOAD_FOLDER'], 'Earring.png')
    PathAcc2 = os.path.join(app.config['UPLOAD_FOLDER'], 'Collar.png')
    PathAcc3 = os.path.join(app.config['UPLOAD_FOLDER'], 'Collar2.png')
    return render_template("Attributes.html",
    hairData = [{'hair': 'Cabelo 1'}, {'hair': 'Cabelo 2'}, {'hair': 'Cabelo 3'}, {'hair': 'Cabelo 4'}],
    sexData = [{'sex': 'F'}, {'sex': 'M'}],
    accData = [{'acc': 'Brinco'}, {'acc': 'Colar 1'}, {'acc': 'Colar 2'}],
    hair1 = PathHair1,
    hair2 = PathHair2,
    hair3 = PathHair3,
    hair4 = PathHair4,
    acc1 = PathAcc1,
    acc2 = PathAcc2,
    acc3 = PathAcc3)

@app.route('/postend', methods=['POST', 'GET'])
def postend():
    nome = request.form['name']
    email = request.form['email']
    hair = request.form['hair']
    sex = request.form['sex']
    acessories = request.form['acce']
    funcs.dbWrite(nome, sex, hair, acessories, email)
    return render_template("postend.html")

@app.route('/initial')
def initial():
    return render_template('initial.html')

@app.route('/photo')
def takingPhoto():
    # tira foto com o open-cv e coloca em uma pasta
    # funcs.takePhoto(1)

    # path onde a foto deverá ficar
    full_filename = os.path.join(app.config['UPLOAD_FOLDER'], 'image.jpg')
   
    # fazer o download da imagem pelo s3
    funcs.downloadS3('avataring-img', full_filename)
    
    # pagina com uma user image
    return render_template("photo.html", user_image = full_filename)


@app.route('/')
def myAvattaringForm():
    return render_template("myAvattaringForm.html")

@app.route("/myavattaring", methods=['POST', 'GET'])
def myAvattaring():
    email = request.form['email']
    filename = email + ".jpg"
    full_filename = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    retFunc = funcs.downloadSpecificS3('avataring-img', filename, full_filename)
    if retFunc is None:
        return render_template("myAvattaring.html", user_image = "static/IMG/404.jpeg")
    else:
        return render_template("myAvattaring.html", user_image = full_filename)

if __name__ == "__main__":
    if not os.path.exists("images"):
        os.mkdir("images")

    app.run(host='0.0.0.0', port=5000)
