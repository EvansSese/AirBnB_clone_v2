#!/usr/bin/python3
""" Function to display states using flask """


from flask import Flask, render_template
from models import storage
from models.place import State


app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def list_states():
    """ Display states in alphabetical order"""
    states = sorted(list(storage.all(State).values()),
                    key=lambda state: state.name)
    return render_template('7-states_list.html',
                           states=states)
