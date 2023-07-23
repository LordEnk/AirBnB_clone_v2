#!/usr/bin/python3
'''simple Flask web application.
'''
from flask import Flask, render_template

from models import storage
from models.state import state

app = Flask(__name__)
'''The Flask application instance.'''
app.url_map.strict_slashes = False

@app.route('/states_list')
def states_list():
	'''The states_list page.'''
	states = sorted(list(storage.all('state').values()), key=lambda state: state.name)
	return render_template('7-states_list.html', states=states)

@app.teardown_appcontext
def teardown_appcontext(exc):
    '''The Flask app/request context end event listener.'''
    storage.close()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
