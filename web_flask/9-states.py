#!/usr/bin/python3
"""
Script that starts a Flask web application
"""

from flask import Flask, render_template
from models import State, storage

app = Flask(__name__)

@app.route('/states', strict_slashes=False)
@app.route('/states/<state_id>', strict_slashes=False)
def states(state_id=None):
    """
    Display the states and cities listed in alphabetical order.

    Args:
        state_id (str, optional): The id of the state.

    Returns:
        rendered_template: Rendered HTML template "9-states.html"
        with the provided states and state id.
    """
    states = storage.all(State)
    if state_id is not None:
        state_id = 'State.' + state_id
    return render_template('9-states.html', states=states, state_id=state_id)

@app.teardown_appcontext
def teardown_db(exception):
    """
    Closes the session on teardown.

    Args:
        exception (Exception): The exception that may have occurred during the request.

    Returns:
        None
    """
    storage.close()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
