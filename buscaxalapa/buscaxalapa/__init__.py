import os

from flask import Flask
from flask_bcrypt import Bcrypt
from sqlalchemy import create_engine 
from sqlalchemy.orm import scoped_session, sessionmaker

app  =  Flask(__name__)
bcrypt = Bcrypt(app)

import buscaxalapa.header

engine = create_engine("postgres://postgres:Barbara1621@localhost:5432/BuscaXalapa")
db = scoped_session(sessionmaker(bind=engine))

    
if __name__ == '__main__':
    app.run(host='0.0.0.0', port = 5000, threaded=True, debug=True)