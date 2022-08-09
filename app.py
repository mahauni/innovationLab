from flask import Flask, render_template, url_for, request, redirect
import os
import funcs
import ast

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = './images'

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
    funcs.takePhoto(1)

    # with open('./tables/table.txt', 'w') as f:
    #   file_contents = f.read()
    #   lista = ast.literal_eval(file_contents)

    # full_filename = os.path.join(app.config['UPLOAD_FOLDER'], './imagens/pic'+ str(lista[len(lista)-1][0] + 1) +'.jpg')
    # return render_template("photo.html", user_image = full_filename)


    # NOT WORKING
    full_filename = './../images/pic1.jpg'
    return render_template("photo.html", user_image = full_filename)

if __name__ == "__main__":
    if not os.path.exists("images"):
        os.mkdir("images")
    app.run(debug=True)