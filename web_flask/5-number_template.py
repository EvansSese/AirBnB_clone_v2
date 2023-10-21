#!/usr/bin/python3
""" C Route"""
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """ Function for home route"""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """ Function for home route"""
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c_with_text(text):
    """ Function to get text from route"""
    text = text.replace('_', ' ')
    return "C " + text


@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_with_text(text):
    """ Function to get text from route, with default value"""
    text = text.replace('_', ' ')
    return "Python " + text


@app.route('/number/<int:n>', strict_slashes=False)
def is_number(n):
    """ Function to display is number """
    return f"{n} is a number"


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    if isinstance(n, int):
        return render_template('5-number.html', n=n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
