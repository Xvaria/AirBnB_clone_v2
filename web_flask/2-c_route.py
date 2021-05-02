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


if __name__ == "__main__":
    app.run(host="0.0.0.0")
