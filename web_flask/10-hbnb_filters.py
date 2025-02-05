#!/usr/bin/python3
""" Function to display HBNB filters """


from flask import Flask, render_template
from models import storage
from models.state import State
from models.amenity import Amenity


app = Flask(__name__)


@app.route('/hbnb_filters', strict_slashes=False)
def states_and_cities():
    """ Display states and cities in alphabetical order"""
    states = storage.all(State).values()
    amenities = storage.all(Amenity).values()
    return render_template('10-hbnb_filters.html',
                           states=states, amenities=amenities)


@app.teardown_appcontext
def teardown(exception):
    """ Close the session """
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
