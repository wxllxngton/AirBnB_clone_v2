#!/usr/bin/python3
"""
Script that starts a Flask web application
"""

from flask import Flask, render_template
from models import State, storage

app = Flask(__name__)

@app.route('/hbnb_filters', strict_slashes=False)
def filters():
    """
    Display a HTML page similar to 6-index.html from the static folder.

    Returns:
        str: Rendered HTML page.
    """
    states = storage.all("State").values()
    amenities = storage.all("Amenity").values()
    return render_template('10-hbnb_filters.html', states=states, amenities=amenities)

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
    app.run(host='0.0.0.0', port=5000)
