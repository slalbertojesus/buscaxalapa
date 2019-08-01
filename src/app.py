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
    #Obtener correo 
    correo = request.form.get("correo")
    #Obtener nombre 
    nombre = request.form.get("nombre")
    #Hasher contraseña y guardarla
    contra = request.form.get("contra")
    contra_hash = bcrypt.generate_password_hash(contra)
    db.execute("insert into Usuario (correo, nombrecompleto, contrasenia) values (:correo, :nombre, :contra)", 
    {"correo": correo, "nombre": nombre, "contra": contra_hash})
    db.commit()
    return render_template("Correct-Process.html", message = "Registro exitoso")

@app.route("/Election")
def Election():
    return render_template("Election-Type.html")

@app.route("/Choosing", methods = ["POST"])
def Choosing():
        if request.form['button-choosing'] == 'business':
            return render_template("Business.html")   
        elif request.form['button-choosing'] == 'service':
            return render_template("Service.html")

@app.route("/Service")
def Service():
    return render_template("Service.html")

@app.route("/Business")
def Business():
    return render_template("Business.html")
    
#hacer que funcione el movimiento entre páginas de servicios


if __name__ == '__main__':
    app.run(host='0.0.0.0', port = 5000, threaded=True, debug=True)
