import os

from flask import Flask


app = Flask(__name__)
from buscaxalapa import views, register, sessions
app.register_blueprint(views.bp)
app.register_blueprint(sessions.bp)
app.register_blueprint(register.bp)
app.add_url_rule("/", endpoint="homepage")
app.run(host='0.0.0.0', port = 5000, threaded=True, debug=True)