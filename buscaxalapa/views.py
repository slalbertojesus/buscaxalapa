from flask import Flask, render_template, request, redirect, url_for, flash
from flask import Blueprint
from flask_bcrypt import Bcrypt
from sqlalchemy.exc import IntegrityError
from itsdangerous import URLSafeTimedSerializer
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
     try:
          correo = request.form.get("correo")
          nombre = request.form.get("nombre")
          contra = request.form.get("contra")
          contra_hash = bcrypt.generate_password_hash(contra)
          usuario = Usuario(correo, nombre, contra_hash)
          session.add(usuario)
          session.commit()
          mandar_confirmacion_correo(usuario.correo)
          flash('Thanks for registering!  Please check your email to confirm your email address.', 'success')
          return redirect(url_for('views.inicio'))
     except IntegrityError:
                db.session.rollback()
                flash('ERROR! Email ({}) already exists.')
     return render_template('register.html')


def mandar_correo(subject, recipients, html_body):
    msg = Message(subject, recipients=recipients)
    msg.html = html_body
    thr = Thread(target=send_async_email, args=[msg])
    thr.start()


def mandar_confirmacion_correo(usuario_correo):
     confirm_serializer = URLSafeTimedSerializer(app.config['SECRET_KEY'])
     
     confirm_url = url_for(
        'token.confirmal_email',
        token= confirm_serializer.dumps(usuario_correo, salt='email-confirmation-salt'),
        _external=True)

     html = render_template(
          'email-confirmation.html',
          confirm_url=confirm_url)
          
     mandar_correo('Confirm Your Email Address', [usuario_correo], html)

@bp.route('/confirmar/<token>')
def confirmar_email(token):
    try:
        confirm_serializer = URLSafeTimedSerializer(app.config['SECRET_KEY'])
        email = confirm_serializer.loads(token, salt='email-confirmation-salt', max_age=3600)
    except:
        flash('The confirmation link is invalid or has expired.', 'error')
        return redirect(url_for('views.index'))
 
    user = Usuario.query.filter_by(correo=correo).first()
 
    if user.correo_confirmado:
        flash('Account already confirmed. Please login.', 'info')
    else:
        user.correo_confirmado = True
        user.correo_confirmado_en = datetime.now()
        db.session.add(user)
        db.session.commit()
        flash('Thank you for confirming your email address!')
 
    return redirect(url_for('recipes.index'))

#TODO mandar correo de confirmación 
#TODO ver que es lo que va a cambiar en el header
#TODO iniciar sesion y cerrar sesión 