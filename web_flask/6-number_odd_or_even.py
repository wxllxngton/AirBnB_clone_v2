#!/usr/bin/python3
"""
Script that starts a Flask web application.
"""

from flask import Flask, render_template

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
def c_text(text):
    """
    Displays "C " followed by the value of the text variable.

    Parameters:
        text (str): The text string to be formatted.

    Returns:
        str: The formatted message "C {formatted_text}"
    """
    formatted_text = text.replace("_", " ")
    return f"C {formatted_text}"


@app.route("/python/<text>", methods=["GET"], strict_slashes=False)
def python_text(text="is cool"):
    """
    Displays "Python " followed by the value of the text variable.

    Parameters:
        text (str, optional): The text string to be printed. Defaults to "is cool".

    Returns:
        str: The formatted message "Python {formatted_text}"
    """
    formatted_text = text.replace("_", " ")
    return f"Python {formatted_text}"


@app.route("/number/<n>", methods=["GET"], strict_slashes=False)
def number_n(n):
    """
    Displays "{n} is a number" only if n is an integer.

    Parameters:
        n (str): The number to be checked.

    Returns:
        str: "{n} is a number" or "{n} is not a valid number."
    """
    try:
        n = int(n)
        return f"{n} is a number"
    except ValueError:
        return f"{n} is not a valid number"


@app.route("/number_template/<n>", methods=["GET"], strict_slashes=False)
def number_template(n):
    """
    Displays an HTML page only if n is an integer.

    Parameters:
        n (str): The number to be displayed.

    Returns:
        rendered_template: Rendered HTML template "5-number.html" with the provided number.
    """
    try:
        n = int(n)
        return render_template("5-number.html", n=n)
    except ValueError:
        return f"{n} is not a valid number"


@app.route("/number_odd_or_even/<n>", methods=["GET"], strict_slashes=False)
def number_odd_or_even(n):
    """
    Display a HTML page only if n is an integer.

    Parameters:
        n (int): An integer number.

    Returns:
        render_template: Rendered HTML template "6-number_odd_or_even.html" with the provided number.
    """
    try:
        n = int(n)
        result = "even" if n % 2 == 0 else "odd"
        return render_template("6-number_odd_or_even.html", result=result, n=n)
    except ValueError:
        return f"{n} is not a valid number"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
