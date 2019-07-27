import os

from flask import Flask, render_template, request
from sqlalchemy import create_engine 
from sqlalchemy.orm import scoped_session, sessionmaker

app  =  Flask(__name__)

engine = create_engine("postgres://postgres:Barbara1621@localhost:5432/BuscaXalapa")
db = scoped_session(sessionmaker(bind=engine))

@app.route("/Index", methods = ["POST"])
def index():
    return render_template("Index.html")

@app.route("/Ingresar", methods = ["POST"])
def  Ingresar():
    return  render_template("Index.html")