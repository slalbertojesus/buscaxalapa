import os 

from flask import Flask 
from sqlalchemy import Column, String, Integer, ForeignKey

from base import Base


class Usuario (Base):
        __tablename__ = 'usuario'

        id = Column(Integer, primary_key = True)
        correo = Column(String, nullable = False)
        nombrecompleto = Column(String, nullable = False)
        contrasenia = Column(String, nullable = False)

        def __init__(self, correo, nombrecompleto, contrasenia):
                self.correo = correo
                self.nombrecompleto = nombrecompleto
                self.contrasenia = contrasenia
