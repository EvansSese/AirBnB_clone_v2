#!/usr/bin/python3
""" C Route"""
from flask import Flask

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


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
