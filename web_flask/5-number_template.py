#!/usr/bin/python3
'''simple web Flask application.
'''
from flask import Flask, escape

app = Flask(__name__)
'''The Flask application instance.'''
app.url_map.strict_slashes = False

@app.route('/')
def home():
        '''The home page.'''
        return 'Hello HBNB!'

@app.route('/hbnb')
def hbnb():
        '''The hbnb page.'''
        return 'HBNB'

@app.route('/c/<text>')
def cpage(text):
        '''The c page.'''
        text = escape(text).replace('_', ' ')
        return f'c {text}'

@app.route('/python/')
@app.route('/python/<text>')
def ppage(text='is _cool'):
        '''The python page.'''
        text = escape(text).replace('_', ' ')
        return f'Python {text}'

@app.route('/number/<int:n>')
def npage(n):
        '''The number page.'''
        return f'{n} is a number'

@app.route('/number_template/<int:n>')
def number_template(n):
	'''The number_template page.'''
	if isinstance(n, int):
		return render_template('5-number.html', number=n)

if __name__ == '__main__':
	app.run(host='0.0.0.0', port='5000')
