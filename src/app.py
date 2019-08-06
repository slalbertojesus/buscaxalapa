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
    
#Metodo en registro
@app.route("/Registro", methods = ["GET","POST"])
def Registro():
    if request.method == 'POST':
        rutaPrevia =    request.path
        if request.form['button-choosing'] == 'Anunciar mi negocio':
            return redirect(url_for("Negocio", rutaPrevia = rutaPrevia))   
        elif request.form['button-choosing'] == 'Anunciar mi servicio':
            return redirect(url_for("Servicio", rutaPrevia = rutaPrevia))
    if request.method == 'GET':
        return render_template("Registro.html")
    return redirect("Error")

@app.route("/Error")
def RoutError():
    return redirect("Correct-Process.html")

@app.route("/<rutaPrevia>/Negocio")
def Negocio(rutaPrevia):
    return render_template("/Business.html")
    
@app.route("/<rutaPrevia>/Servicio")
def Servicio(rutaPrevia):
    return render_template("/Service.html")

#TODO Tiene que tener el camino hacia ese URL completo ej Registra/Negocio/Restaurante utilizar endpoints
@app.route("/Registro/Negocio", methods = ["POST"])
def redireccionaFormatoNegocio():
    identificadorNegocio = request.form['negocio-escogido']
    return redirect(url_for('despliegaFormaNegocio', identificadorNegocio = identificadorNegocio))

@app.route("/Registro/Negocio/<identificadorNegocio>")
def despliegaFormaNegocio(identificadorNegocio):
        return render_template("/Business-Creation.html")
    
if __name__ == '__main__':
    app.run(host='0.0.0.0', port = 5000, threaded=True, debug=True)