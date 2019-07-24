from flask import Flask, render_template

app  =  Flask(__name__)

@app.route("/")
def  Index():
    headline = "Busca Xalapa"
    return  render_template("Sessions.html", headline = headline)