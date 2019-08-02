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

@app.route("/Anuncio")
def Area():
    return render_template("Election-Type.html")

@app.route("/Escoge", methods = ["POST"])
def Escoge():
        rutaPrevia = "Anuncio"
        if request.form['button-choosing'] == 'Negocio':
            return redirect(url_for("Negocio",  rutaPrevia = rutaPrevia))   
        elif request.form['button-choosing'] == 'Servicio':
            return redirect(url_for("Servicio", rutaPrevia = rutaPrevia))

@app.route("/<rutaPrevia>/Negocio")
def Negocio(rutaPrevia):
    return render_template("/Business.html")
    
@app.route("/<rutaPrevia>/Servicio")
def Servicio(rutaPrevia):
    return render_template("Service.html")

@app.route("/Registroadd", methods = ["POST"])
def  Registroadd():
    correo = request.form.get("correo")
    nombre = request.form.get("nombre")
    contra = request.form.get("contra")
    contra_hash = bcrypt.generate_password_hash(contra)
    db.execute("insert into Usuario (correo, nombrecompleto, contrasenia) values (:correo, :nombre, :contra)", 
    {"correo": correo, "nombre": nombre, "contra": contra_hash})
    db.commit()
    return render_template("Correct-Process.html", message = "Registro exitoso")
    
if __name__ == '__main__':
    app.run(host='0.0.0.0', port = 5000, threaded=True, debug=True)
