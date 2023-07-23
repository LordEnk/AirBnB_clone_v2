#!/usr/bin/python3
'''simple Flask web application.
'''
from flask import Flask, escape


app = Flask(__name__)
'''The Flask application instance.'''
app.url_map.strict_slashes = False


@app.route('/')
def home():
	'''The home page'''
	return 'Hello HBNB!'

@app.route('/hbnb')
def hbnb():
	'''The hbnb page'''
	return 'HBNB'

@app.route('/c/<text>')
def cpage(text):
	'''The c page'''
	text = escape(text).replace('_', ' ')
	return f'C {text}'

if __name__ == '__main__':
	app.run(host='0.0.0.0', port='5000')
