#!/usr/bin/python3
from flask import Flask


app = Flask(__name__)
app.url_map.strick_slashes = False


@app.route('/')
def hello_hbnb():
    return 'Hello HBNB!'


@app.route('/hbnb')
def hbnb():
    return 'HBNB'


@app.route('/c/<text>')
def c_is(text):
    return 'c {}'.format(text)


@app.route('/python/<text>')
def python_is(text='is cool'):
    return 'Python {}'.format(text)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
