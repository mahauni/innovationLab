from flask import Flask, render_template, url_for, request, redirect
import os
import funcs
import ast

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = os.path.join('static', 'IMG')

@app.route('/form')
def index():
    return render_template("Attributes.html",
    hairData = [{'hair': 'Encaracolado'}, {'hair': 'Longo'}, {'hair': 'Curto'}, {'hair': 'Tijela'}],
    sexData = [{'sex': 'F'}, {'sex': 'M'}],
    accData = [{'acc': 'Brinco'}, {'acc': 'Colar'}])

@app.route('/postend', methods=['POST', 'GET'])
def postend():
    nome = request.form['name']
    email = request.form['email']
    hair = request.form['hair']
    sex = request.form['sex']
    acessories = request.form['acce']
    funcs.dbWrite(nome, sex, hair, acessories, email)
    return render_template("postend.html")

@app.route('/')
def initial():
    return render_template('initial.html')

@app.route('/photo')
def takingPhoto():
    funcs.takePhoto(1)

    full_filename = os.path.join(app.config['UPLOAD_FOLDER'], 'image.jpg')
    return render_template("photo.html", user_image = full_filename)

if __name__ == "__main__":
    if not os.path.exists("images"):
        os.mkdir("images")

    if not os.path.exists("./static/IMG"):
        os.mkdir("./static/IMG")

    app.run(debug=True)