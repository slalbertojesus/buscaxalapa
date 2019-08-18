import os

from flask import Flask

def create_app():
    app = Flask(__name__, instance_relative_config=True)
    from buscaxalapa import views, register
    app.register_blueprint(views.bp)
    app.register_blueprint(register.bp)
    app.add_url_rule("/", endpoint="index")
    app.run(host='0.0.0.0', port = 5000, threaded=True, debug=True)
    return app