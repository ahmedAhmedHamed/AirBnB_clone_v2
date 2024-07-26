#!/usr/bin/python3
"""simply a hello_world!"""
from flask import Flask

app = Flask(__name__)

@app.route("/", strict_slashes=False)
def hello_world():
    """the / route that prints hello hbnb!"""
    return "Hello HBNB!"
