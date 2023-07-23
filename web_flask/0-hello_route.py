#!/usr/bin/python3
'''A simple flask web application
'''
from flask import Flask

app = Flask(__name__)
'''The flask application instance'''

@app.route('/', strict_slashes=False)
def index():
	'''The home page'''
	return 'Hello HBNB!'

if __name__ == '__main__':
	app.run(host='0.0.0.0', port='5000')
