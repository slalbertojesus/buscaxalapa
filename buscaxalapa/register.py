from flask import Flask, render_template, request, redirect, url_for
from flask import Blueprint
from sqlalchemy import create_engine 
from sqlalchemy.orm import scoped_session, sessionmaker

bp = Blueprint("register", __name__)

# #Metodo en registro
# @app.route("/Registro", methods = ["GET","POST"])
# def Registro():
#     if request.method == 'POST':
#         rutaPrevia =    request.path
#         if request.form['button-choosing'] == 'Anunciar mi negocio':
#             return redirect(url_for("Negocio", rutaPrevia = rutaPrevia))   
#         elif request.form['button-choosing'] == 'Anunciar mi servicio':
#             return redirect(url_for("Servicio", rutaPrevia = rutaPrevia))
#     if request.method == 'GET':
#         return render_template("Registro.html")
#     return redirect("Error")

# @app.route("/Error")
# def RoutError():
#     return redirect("Correct-Process.html")

# @app.route("/<rutaPrevia>/Negocio")
# def Negocio(rutaPrevia):
#     return render_template("/Business.html")
    
# @app.route("/<rutaPrevia>/Servicio")
# def Servicio(rutaPrevia):
#     return render_template("/Service.html")

# #TODO Separar archivos 
# @app.route("/Registro/Negocio", methods = ["POST"])
# def redireccionaFormatoNegocio():
#     identificadorNegocio = request.form['negocio-escogido']
#     return redirect(url_for('despliegaFormaNegocio', identificadorNegocio = identificadorNegocio))

# @app.route("/Registro/Negocio/<identificadorNegocio>")
# def despliegaFormaNegocio(identificadorNegocio):
#         return render_template("/Business-Creation.html")
