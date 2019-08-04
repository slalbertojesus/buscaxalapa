import os

from flask import Flask, render_template, request, redirect, url_for
from flask_bcrypt import Bcrypt
from sqlalchemy import create_engine 
from sqlalchemy.orm import scoped_session, sessionmaker

app  =  Flask(__name__)
bcrypt = Bcrypt(app)

engine = create_engine("postgres://postgres:Barbara1621@localhost:5432/BuscaXalapa")
db = scoped_session(sessionmaker(bind=engine))

@app.route("/Index")
def Index():
    return render_template("Index.html")

##Redireccionamiento de header
@app.route("/EscogeHeader", methods = ["POST"])
def EscogeHeader():
        if request.form['button'] == 'Conocenos':
            return redirect(url_for("Conocenos"))   
        elif request.form['button'] == 'Roomie':
            return redirect(url_for("Roomie"))

@app.route("/Roomie")
def Roomie():
    return render_template("/Roomie.html")
##Redireccionamiento de header


@app.route("/Ingreso", methods = ["POST"])
def  Ingreso():
    correo = request.form.get("correo")
    nombre = request.form.get("nombre")
    contra = request.form.get("contra")
    contra_hash = bcrypt.generate_password_hash(contra)
    db.execute("insert into Usuario (correo, nombrecompleto, contrasenia) values (:correo, :nombre, :contra)", 
    {"correo": correo, "nombre": nombre, "contra": contra_hash})
    db.commit()
    return render_template("Correct-Process.html", message = "Registro exitoso")

@app.route("/Registro")
def Area():
    return render_template("Registro.html")

#Metodo en registro
@app.route("/Escoge", methods = ["POST"])
def Escoge():
        rutaPrevia = "Registro"
        if request.form['button-choosing'] == 'Anunciar mi negocio':
            return redirect(url_for("Negocio", rutaPrevia = rutaPrevia))   
        elif request.form['button-choosing'] == 'Anunciar mi servicio':
            return redirect(url_for("Servicio", rutaPrevia = rutaPrevia))

@app.route("/<rutaPrevia>/Negocio")
def Negocio(rutaPrevia):
    return render_template("/Business.html")
    
@app.route("/<rutaPrevia>/Servicio")
def Servicio(rutaPrevia):
    return render_template("/Service.html")

@app.route("/RegistroNegocio", methods = ["POST"])
def RegistroNegocio():
    url = request.referrer
    identificadorNegocio = request.form['negocio-escogido']
    return redirect(url_for('CreaNegocio', identificadorNegocio = identificadorNegocio))

@app.route("/<identificadorNegocio>")
def   CreaNegocio(identificadorNegocio):
        return render_template("/Business-Creation.html")
    
if __name__ == '__main__':
    app.run(host='0.0.0.0', port = 5000, threaded=True, debug=True)
