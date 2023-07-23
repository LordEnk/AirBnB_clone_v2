#!/usr/bin/python3
'''simple Flask web application.
'''
from flask import Flask, render_template
from models import storage
from models.amenity import Amenity
from models.place import Place
from models.state import State
from models.city import City

app = Flask(__name__)
'''The Flask application instance.'''
app.url_map.strict_slashes = False


@app.route('/hbnb')
def hbnb():
	'''The hbnb page.'''
	states = sorted(list(storage.all(State).values()), key=lambda state: state.name)
	cities = sorted(list(storage.all(City).values()), key=lambda city: city.name)
	amenities = sorted(list(storage.all(Amenity).values()), key=lambda amenity: amenity.name)
	places = sorted(list(storage.all(Place).values()), key=lambda place: place.name)
	return render_template('100-hbnb.html', states=states, cities=cities, amenities=amenities, places=places)

@app.teardown_appcontext
def teardown_appcontext(excemption):
    '''The Flask app/request context end event listener.'''
    storage.close()


if __name__ == '__main__':
	app.run(host='0.0.0.0' port=5000)
