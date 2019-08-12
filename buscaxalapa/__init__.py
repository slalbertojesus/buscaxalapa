import os

from flask import Flask
import buscaxalapa.views

def create_app():
    app = Flask(__name__, instance_relative_config=True)
    from buscaxalapa import views 
    app.register_blueprint(views.bp)
    app.add_url_rule("/", endpoint="index")
    app.run(host='0.0.0.0', port = 5000, threaded=True, debug=True)
    return app