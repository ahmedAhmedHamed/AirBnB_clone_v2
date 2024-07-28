#!/usr/bin/python3
"""
houses the hello route solution
"""
from flask import Flask, render_template
from models import storage
from models.state import State
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
	text = text.replace("_", ' ')
	return f"C {text}"


@app.route("/python/", defaults={'text': 'is cool'}, strict_slashes=False)
@app.route("/python/(<text>)", strict_slashes=False)
def python_route(text):
	"""
	the route that prints python + variable !
	"""
	text = text.replace("_", ' ')
	return f"Python {text}"


@app.route("/number/<int:n>", strict_slashes=False)
def number_route(n):
	"""
	display “n is a number” only if n is an integer
	"""
	return f"{n} is a number"


@app.route("/number_template/<int:n>", strict_slashes=False)
def number_template_route(n):
	"""
	display “n is a number” only if n is an integer
	"""
	return render_template('5-number.html', number=n)


@app.route("/number_odd_or_even/<int:n>", strict_slashes=False)
def number_odd_or_even_template_route(n):
	"""
	display “n is a number” only if n is an integer
	H1 tag: “Number: n is even|odd” inside the tag BODY
	"""
	evenness = "odd"
	if n % 2 == 0:
		evenness = "even"
	return render_template('6-number_odd_or_even.html', number=n, evenness=evenness)


@app.route("/states_list", strict_slashes=False)
def states_list():
	"""
	display “n is a number” only if n is an integer
	"""
	states = list(storage.all(State).values())
	states.sort(key=lambda x: x.name)
	return render_template('7-states_list.html', states=states)


@app.teardown_appcontext
def teardown(e):
	storage.close()


if __name__ == '__main__':
	"""
	this is the main that runs the app
	"""
	app.run(host='0.0.0.0', port=5000, debug=False)
