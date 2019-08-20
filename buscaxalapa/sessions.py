from flask import Flask, render_template, request, redirect, url_for
from flask import Blueprint
from sqlalchemy import create_engine 
from sqlalchemy.orm import scoped_session, sessionmaker

bp = Blueprint("sessions", __name__)

engine = create_engine("postgres://postgres:Barbara1621@localhost:5432/BuscaXalapa")
db = scoped_session(sessionmaker(bind=engine))


@bp.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.get(form.email.data)
        if user:
            if bcrypt.check_password_hash(user.password, form.password.data):
                user.authenticated = True
                db.session.add(user)
                db.session.commit()
                login_user(user, remember=True)
                return redirect(url_for("bull.reports"))
return render_template("login.html", form=form)

# TODO Añadir clases de usuario
# TODO Crear dao para acceso a db 
# TODO Separar metodos para abrir y cerrar conexionens en db 
# TODO Checar password hasheada
# TODO Revisar que es lo que va a cambiar cuando el usuario esté logueado
# TODO Hacer cambios al header para que se cambie lo de iniciar sesion - ingresar