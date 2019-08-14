from flask import Flask, render_template, request, redirect, url_for
from flask import Blueprint
from sqlalchemy import create_engine 
from sqlalchemy.orm import scoped_session, sessionmaker

bp = Blueprint("views", __name__)

engine = create_engine("postgres://postgres:Barbara1621@localhost:5432/BuscaXalapa")
db = scoped_session(sessionmaker(bind=engine))

@bp.route("/")
def index():
    return render_template("index.html")

@bp.route("/Roomie")
def roomie():
    return render_template("roomie.html")

@bp.route("/Compra-vende")
def marketplace():
    return render_template("marketplace.html")

@bp.route("/Trabajos")
def jobs():
    return render_template("jobs.html")

@bp.route("/Ingreso", methods=["POST"])
def Ingreso():
     correo = request.form.get("correo")
     nombre = request.form.get("nombre")
     contra = request.form.get("contra")
     contra_hash = bcrypt.generate_password_hash(contra)
     db.execute("insert into Usuario (correo, nombrecompleto, contrasenia) values (:correo, :nombre, :contra)",
                {"correo": correo, "nombre": nombre, "contra": contra_hash})
     db.commit()
     return render_template("Correct-Process.html", message="Registro exitoso")
    
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
