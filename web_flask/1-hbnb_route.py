#!/usr/bin/python3
'''A simple web flask application
'''

from flask import Flask

app = Flask(__name__)
'''The Flask application instance'''
app.url_map.strict_slashes = False

# Route for the home page
@app.route('/')
def home():
	'''the Home page'''
	return 'Hello HBNB!'

# Route for /hbnb
@app.route('/hbnb')
def hbnb():
	'''The hbnb page'''
	return 'HBNB'

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=5000)
