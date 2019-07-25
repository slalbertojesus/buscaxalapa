from flask import Flask, render_template

app  =  Flask(__name__)

@app.route("/")
def  Index():
    return  render_template("Sessions.html")

@app.route("/Service")
def Service():
    return render_template("Service.html")

@app.route("/Homepage")
def  Homepage():
    return render_template("HomePage.html")