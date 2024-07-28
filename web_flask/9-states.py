#!/usr/bin/python3
"""
houses the hello route solution
"""
from flask import Flask, render_template
from models import storage, City
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


@app.route("/cities_by_states", strict_slashes=False)
def cities_by_states():
	"""
	display cities_by_states
	"""
	states = list(storage.all(State).values())
	sent = []
	states.sort(key=lambda x: x.name)
	for state in states:
		tempdict = {"id": state.id, "name": state.name, "cities": state.cities}

		sent.append(tempdict)

	return render_template('8-cities_by_states.html', states=sent)


@app.route("/states", strict_slashes=False)
def all_states():
	"""
	display “n is a number” only if n is an integer
	"""
	return states_list()


@app.route("/states/<id>", strict_slashes=False)
def one_state(id):
	"""
	display cities_by_states filtering by id
	"""
	states = list(storage.all(State).values())
	sent_state = None
	for state in states:
		if state.id == id:
			sent_state = state
	states.sort(key=lambda x: x.name)
	if sent_state:
		tempdict = {"id": sent_state.id, "name": sent_state.name, "cities": sent_state.cities}
	else:
		tempdict = {}
	return render_template('9-states.html', state=tempdict)



@app.teardown_appcontext
def teardown(e):
	storage.close()


if __name__ == '__main__':
	"""
	this is the main that runs the app
	"""
	app.run(host='0.0.0.0', port=5000, debug=False)
