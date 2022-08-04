from flask import Flask, render_template, url_for, request, redirect
import os
import funcs

app = Flask(__name__)

@app.route('/form')
def index():
    return render_template("index.html",
    hairData = [{'hair': 'Encaracolado'}, {'hair': 'Longo'}, {'hair': 'Curto'}, {'hair': 'Tijela'}],
    sexData = [{'sex': 'F'}, {'sex': 'M'}],
    accData = [{'acc': 'Brinco'}, {'acc': 'Colar'}])

@app.route('/postend', methods=['POST', 'GET'])
def postend():
    nome = request.form['nome']
    email = request.form['email']
    hair = request.form.get('hair')
    sex = request.form.get('sex')
    acessories = request.form.get('acce')
    funcs.dbWrite(nome, sex, hair, acessories, email)
    return render_template("postend.html")

@app.route('/')
def initial():
    return render_template('initial.html')

@app.route('/photo')
def takingPhoto():
    funcs.takePhoto()
    return render_template("index.html arrumar aqui")

if __name__ == "__main__":
    if not os.path.exists("images"):
        os.mkdir("images")
    app.run(debug=True)