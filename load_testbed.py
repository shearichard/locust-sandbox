"""
load_testbed.py

A tiny Flask app to point the Locust load testing tool at.
"""

from flask import Flask
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


if __name__ == "__main__":
    app.run()
