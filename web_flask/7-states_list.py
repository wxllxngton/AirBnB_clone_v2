#!/usr/bin/python3
"""
Script that starts a Flask web application
"""

from flask import Flask, render_template
from models import State, storage

app = Flask(__name__)

@app.route('/states_list', strict_slashes=False)
def states_list():
    """
    Renders an HTML page with the states listed in alphabetical order.

    Returns:
        rendered_template (str): Rendered HTML template "7-states_list.html"
        with the provided states sorted by state name.
    """
    states = sorted(list(storage.all(State).values()), key=lambda x: x.name)
    return render_template('7-states_list.html', states=states)

@app.teardown_appcontext
def teardown_db(exception):
    """
    Closes the session on teardown.

    Parameters:
        exception (Exception): The exception that may have occurred during the request.

    Returns:
        None
    """
    storage.close()

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
