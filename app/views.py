from app import app
from flask import render_template
import requests


@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html")

@app.route("/name/<name>")
@app.route("/name")
def name(name = "World"):
    return render_template("name.html",name=name)

@app.route("/dog")
def dog():
    respons = requests.get("https://random.dog/woof.json")
    url = respons.json()
    return render_template("dog.html", image=url['url'])
