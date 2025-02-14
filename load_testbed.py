"""
load_testbed.py

A tiny Flask app to point the Locust load testing tool at.
"""

from flask import Flask, request
from random import randint
from time import sleep

app = Flask(__name__)


@app.route("/")
def index():
    return "Index"


@app.route("/about")
def about():
    return "About ..."


@app.route("/random")
def random():
    delay = randint(0, 2)
    sleep(delay)
    return f"Random delay of {delay}"


@app.route("/item")
def item():
    itm_rqtd = request.args["id"]
    print(f"Item requested was {itm_rqtd}")
    return "Item ..."


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        return "LOGIN_POST"
    else:
        return "LOGIN_GET"


if __name__ == "__main__":
    app.run()
