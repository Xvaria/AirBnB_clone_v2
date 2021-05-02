#!/usr/bin/python3
'''starts a Flask web application'''
from flask import Flask


app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route("/")
def home():
    '''Show index to web page'''
    return("Hello HBNB!")


@app.route("/hbnb")
def HBNB():
    '''Show HBNB web page'''
    return("HBNB")


@app.route("/c/<text>")
def c(text):
    '''Show c web page'''
    return("C {}".format(text.replace('_', ' ')))


@app.route("/python")
@app.route("/python/<text>")
def python(text='is cool'):
    '''Show python web page'''
    return("Python {}".format(text.replace('_', ' ')))


@app.route("/number/<int:n>")
def number(n):
    '''Show number web page'''
    return("{} is a number".format(n))


if __name__ == "__main__":
    app.run(host="0.0.0.0")
