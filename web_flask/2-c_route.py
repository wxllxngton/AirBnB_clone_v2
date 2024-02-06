#!/usr/bin/python3
"""
Script that starts a Flask web application.
"""

from flask import Flask

app = Flask(__name__)


@app.route("/", methods=["GET"], strict_slashes=False)
def index():
    """
    Displays "Hello HBNB!"

    Returns:
        str: The message "Hello HBNB!"
    """
    return "Hello HBNB!"


@app.route("/hbnb", methods=["GET"], strict_slashes=False)
def hbnb():
    """
    Displays "HBNB."

    Returns:
        str: The message "HBNB."
    """
    return "HBNB"


@app.route("/c/<text>", methods=["GET"], strict_slashes=False)
def c_is_fun(text):
    """
    Displays "C " followed by the value of the text variable.

    Parameters:
        text (str): The text string to be formatted.

    Returns:
        str: The formatted message "C {formatted_text}"
    """
    formatted_text = text.replace("_", " ")
    return f"C {formatted_text}"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
