#!/usr/bin/python3
from flask import Flask


app = Flask(__name__)
app.url_map.strick_slashes = False

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/hbnb')
def hbnb():
    return 'HBNB'
