#!/usr/bin/python3
""" A script that starts a Flask web application:
Your web application must be listening on 0.0.0.0, port 5000
"""

from flask import Flask

app = Flask("__name__")


@app.route('/', strict_slashes=False)
def hello():
    """Return a specific string"""
    return ("Hello HBNB!")


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """Returns a certain string"""
    return ("HBNB")


@app.route("/c/<text>", strict_slashes=False)
def cText(text):
    """displays C followed by value of the text variable"""
    return "C {}".format(text.replace("_", " "))


@app.route('/python', strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def pythonText(text="is cool"):
    """displays Python followed by value of the text variable"""
    return "Python {}".format(text.replace("_", " "))


@app.route("/number/<int:n>", strict_slashes=False)
def isNumber(n):
    """displays “n is a number” only if n is an integer"""
    if isinstance(n, int):
        return "{} is a number".format(n)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=None)
