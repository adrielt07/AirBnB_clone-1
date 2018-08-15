#!/usr/bin/python3

from flask import Flask, render_template
from models import storage
from models.state import State
from models.city import City

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


@app.route('/cities_by_states')
def cities_states():
    states_dict = storage.all(State)
    cities_dict = storage.all(City)
    all_cities = []
    new_dict = {}
    for k, v in states_dict.items():
        for ck, cv in cities_dict.items():
            if k.split('.')[1] == cv.state_id:
                all_cities.append(cv)
        new_dict[v] = all_cities
        all_cities = []
    return render_template('8-cities_by_states.html', new_dict=new_dict)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
