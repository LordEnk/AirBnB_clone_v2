#!/usr/bin/python3
'''A simple Flask web application.
'''
from flask import Flask, render_template
from models import storage
from models.amenity import Amenity
from models.state import State
from models.city import City


app = Flask(__name__)
'''The Flask application instance.'''
app.url_map.strict_slashes = False


@app.route('/hbnb_filters')
def hbnb_filters():
	'''The hbnb_flters page'''
	states = sorted(list(storage.all(State).values()), key=lambda state: state.name)
	cities = sorted(list(storage.all(City).values()), key=lambda city: city.name)
	amenities = sorted(list(storage.all(Amenities).values()), key=lambda amenity: amenity.name)
	return render_template('10-hbnb_filters.html', states=states, cities=cities, amenities=amenities)

@app.teardown_appcontext
def teardown_appcontext(exeception)
	'''Teardown appcontext to close SQLAlchemy session after each request'''
	storage.close()

if __name__ == '__main__':
	app.run(host='0.0.0.0', port='5000')
