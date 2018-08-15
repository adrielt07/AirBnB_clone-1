#!/usr/bin/python3

from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.teardown_appcontext
def teardown(exception):
    storage.close()


@app.route('/states_list')
def states_list():
    states_dict = storage.all(State)
    all_states = []
    for k, v in states_dict.items():
        all_states.append(v)
    return render_template('7-states_list.html', all_states=all_states)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
