#!/usr/bin/python3
"""
Script that starts a Flask web application
"""

from flask import Flask, render_template
from models import State, storage

app = Flask(__name__)

@app.route('/cities_by_states', strict_slashes=False)
def cities_by_states():
    """
    Renders an HTML page with the states and their cities
    listed in alphabetical order.

    Returns:
        rendered_template: Rendered HTML template "8-cities_by_states.html"
        with the provided states.
    """
    states = sorted(list(storage.all(State).values()), key=lambda x: x.name)
    return render_template('8-cities_by_states.html', states=states)

@app.teardown_appcontext
def teardown_db(exception):
    """
    Closes the session on teardown

    Parameters:
        exception (error): The error to be thrown

    Returns:
        None
    """
    storage.close()

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
