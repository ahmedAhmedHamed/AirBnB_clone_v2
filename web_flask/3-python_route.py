#!/usr/bin/python3
"""
houses the hello route solution
"""
from flask import Flask

app = Flask(__name__)

@app.route("/", strict_slashes=False)
def hello_world():
    """
    the / route that prints hello hbnb!
    """
    return "Hello HBNB!"

@app.route("/hbnb", strict_slashes=False)
def hbnb_only():
    """
    the / route that prints HBNB!
    """
    return "HBNB"

@app.route("/c/<text>", strict_slashes=False)
def c_route(text):
    """
    the / route that prints c + variable !
    """
    return f"C {text}"

@app.route("/python/", defaults={'text': 'is cool'}, strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python_route(text):
    """
    the / route that prints c + variable !
    """
    return f"Python {text}"

if __name__ == '__main__':
    """
    this is the main that runs the app
    """
    app.run(host='0.0.0.0', port='5000', debug=False)
