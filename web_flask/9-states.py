#!/usr/bin/python3

from flask import Flask, render_template
from models import storage
from models.state import State
from models.city import City

app = Flask(__name__)
app.url_map.strict_slashes = False
app.jinja_env.trim_blocks = True
app.jinja_env.lstrip_blocks = True


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


@app.route('/states')
@app.route('/states/<id>')
def states(id=None):
    states_dict = storage.all(State)
    cities_dict = storage.all(City)
    a_list = []
    if id is not None:
        key = "State." + id
        try:
            all_states = states_dict[key]
        except:
            return render_template('9-states.html', status="Not found!",
                                   loop="Nothing")

        for v in cities_dict.values():
            if v.state_id == id:
                a_list.append(v)
        return render_template('9-states.html',
                               status="State: {}".format(all_states.name),
                               a_list=a_list, loop="cities")

    a_list = states_dict.values()
    return render_template('9-states.html', status="States",
                           a_list=a_list, loop="states")


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
