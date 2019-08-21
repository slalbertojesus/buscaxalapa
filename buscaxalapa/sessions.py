from flask import Flask, render_template, request, redirect, url_for
from flask import Blueprint
from sqlalchemy import create_engine 
from sqlalchemy.orm import scoped_session, sessionmaker
from base import Session, engine, Base

Base.metadata.create_all(engine)

session = Session()

bp = Blueprint("sessions", __name__)

@bp.route("/Entrar", methods=["GET", "POST"])
def login():
    correo = request.form.get("correo")
    nombre = request.form.get("nombre")
    contra = request.form.get("contra")
        #creación de usuario con atributos
        #checar que el usuario no sea nullo 
        #checar hasheo 
        #añadir sesión
        #retorna pagina si esta logueado
    #retornar pagina que no esta logueado

# TODO Añadir clases de usuario
# TODO Crear dao para acceso a db 
# TODO Separar metodos para abrir y cerrar conexionens en db 
# TODO Checar password hasheada
# TODO Revisar que es lo que va a cambiar cuando el usuario esté logueado
# TODO Hacer cambios al header para que se cambie lo de iniciar sesion - ingresar