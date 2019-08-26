from flask import Flask, render_template, request, redirect, url_for
from flask import Blueprint
from flask_bcrypt import Bcrypt
from sqlalchemy import create_engine 
from sqlalchemy.orm import scoped_session, sessionmaker
from base import Session, engine, Base
from Usuario import Usuario
from buscaxalapa import app

bcrypt = Bcrypt(app)

Base.metadata.create_all(engine)

session = Session()

bp = Blueprint("views", __name__)

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

@bp.route("/Inicio")
def homepage():
     return render_template("homepage.html")

@bp.route("/Ingreso", methods=["POST"])
def Ingreso():
     correo = request.form.get("correo")
     nombre = request.form.get("nombre")
     contra = request.form.get("contra")
     contra_hash = bcrypt.generate_password_hash(contra)
     usuario = Usuario(correo, nombre, contra_hash)
     session.add(usuario)
     session.commit()
     session.close()

      subject = "Confirm your email"

        token = ts.dumps(self.email, salt='email-confirm-key')

        confirm_url = url_for(
            'confirm_email',
            token=token,
            _external=True)

        html = render_template(
            'email/activate.html',
            confirm_url=confirm_url)

        mandar_confirmacion_correo(usuario.correo)

     return render_template("Correct-Process.html", message="Registro exitoso")

def mandar_confirmacion_correo(usuario_correo):
    confirm_serializer = URLSafeTimedSerializer(app.config['SECRET_KEY'])
    confirm_url = url_for(
        'users.confirm_email',
        token=confirm_serializer.dumps(user_email, salt='email-confirmation-salt'),
        _external=True)
    html = render_template(
        'email_confirmation.html',
        confirm_url=confirm_url)
    send_email('Confirm Your Email Address', [user_email], html)

#TODO mandar correo de confirmación 
#TODO ver que es lo que va a cambiar en el header
#TODO iniciar sesion y cerrar sesión 