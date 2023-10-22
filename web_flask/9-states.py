#!/usr/bin/python3
""" Function to display state and city using flask """


from flask import Flask, render_template
from models import storage
from models.state import State


app = Flask(__name__)


@app.route('/states', strict_slashes=False)
@app.route('/states/<id>', strict_slashes=False)
def list_states(id=None):
    """ Display states in alphabetical order"""
    states = storage.all(State)
    if id is not None:
        id = 'State.' + id
    return render_template('9-states.html',
                           states=states, id=id)


@app.teardown_appcontext
def teardown(exception):
    """ Close the session """
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
