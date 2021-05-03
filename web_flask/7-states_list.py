#!/usr/bin/python3
""" Start flask app web, using storage engine """
from models import storage
from flask import render_template
from models.state import State
from flask import Flask


app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/states_list')
def states_list():
    """ Index to display lists """
    states = storage.all(State)
    states_list = {}
    for key, value in states.items():
        states_list[value.name] = value
    return render_template('7-states_list.html', states_list=states_list)


@app.teardown_appcontext
def close(states):
    ''' Close the connection with db '''
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0')
