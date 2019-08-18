from flask import Flask, render_template, request, redirect, url_for
from flask import Blueprint
from sqlalchemy import create_engine 
from sqlalchemy.orm import scoped_session, sessionmaker

bp = Blueprint("register", __name__)

# #Metodo en registro
@bp.route("/Registro", methods=["GET", "POST"])
def registro():
     if request.method == 'POST':
         rutaPrevia = request.path
         if request.form['button-choosing'] == 'Anunciar mi negocio':
             return redirect(url_for("register.negocio", rutaPrevia=rutaPrevia))
         elif request.form['button-choosing'] == 'Anunciar mi servicio':
             return redirect(url_for("register.servicio", rutaPrevia=rutaPrevia))
     if request.method == 'GET':
         return render_template("Registro.html")
     return redirect("Error")

@bp.route("/Error")
def RoutError():
     return redirect("Correct-Process.html")

@bp.route("/<rutaPrevia>/Negocio")
def negocio(rutaPrevia):
     return render_template("business.html")

@bp.route("/<rutaPrevia>/Servicio")
def servicio(rutaPrevia):
     return render_template("service.html")

# #TODO Separar archivos
@bp.route("/Registro/Negocio", methods=["POST"])
def redireccionaFormatoNegocio():
     identificadorNegocio = request.form['negocio-escogido']
     return redirect(url_for('register.despliegaFormaNegocio', identificadorNegocio=identificadorNegocio))

@bp.route("/Registro/Negocio/<identificadorNegocio>")
def despliegaFormaNegocio(identificadorNegocio):
         return render_template("/Business-Creation.html")
