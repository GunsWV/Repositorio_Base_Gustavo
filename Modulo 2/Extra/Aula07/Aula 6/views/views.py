from app import app
from flask import render_template

@app.route('/')
def index():
    return render_template("index.html")


@app.route('/faleconosco')
def faleconosco():
    return render_template("faleconosco.html")


@app.route('/cardapio')
def cardapio():
    return render_template("cardapio.html")

@app.route('/maispedidos')
def maispedidos():
    return render_template("maispedidos.html")

