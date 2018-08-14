#!/usr/bin/python3
from flask import Flask


app = Flask(__name__)
app.url_map.strick_slashes = False

@app.route('/')
def hello_hbnb():
    return 'Hello HBNB!'

def hbnb():
    return 'HBNB'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)