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
    """
    create a route '/states_list'
    """
    states_dict = storage.all(State)
    all_states = []
    for k, v in states_dict.items():
        all_states.append(v)
    return render_template('7-states_list.html', all_states=all_states)


@app.route('/cities_by_states')
def cities_states():
    """
    create a route '/cities_by_states'
    """
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
    """
    Create a route '/states' and '/states/<id>'
    """
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


@app.route('/hbnb_filters')
def hbnbfilters():
    """
    create a route '/hbnb_filters'
    """
    all_amenities = storage.all('Amenity')
    all_states = storage.all('State')
    return render_template('10-hbnb_filters.html', all_amenities=all_amenities,
                           all_states=all_states)

@app.route('/hbnb')
def hbnb_is_alive():
    """
    create a route '/100-hbtn'
    """
    all_amenities = storage.all('Amenity')
    all_states = storage.all('State')
    all_places = storage.all('Place')
    all_users = storage.all('User')
    return render_template('100-hbnb.html', all_amenities=all_amenities,
                           all_states=all_states, all_places=all_places,
                           all_users=all_users)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
