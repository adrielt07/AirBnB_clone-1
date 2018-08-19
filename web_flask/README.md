## 0x04. AirBnB clone - Web framework

This project is about udnerstanding Web Framework.
- How to build a web framework with Flask.
- What is route and template.
- How to create an HTML response in Flask by using a template
- How to create a dynamic template (loops, conditions...)
- How to display in HTML data from a MySQL database

Install Flask
```sudo pip3 install flask```

Document:
IP: 0.0.0.0 Port: 5000
To test:
1. from AirBnB_v2 directory
2. Run: python3 -m web_flask.filename
   - Example: python3 -m web_flask.0-hello_route
3. From a different tab
   - curl 0.0.0.0:5000 ; echo "" | cat -e

## Tasks:
- 0-hello_route.py - script that starts a Flask web application
- 1-hbnb_route.py - From 0-hello_route.py. Added new Routes: '/' display "Hello HBNB!". '/hbnb' display "HBNB"
- 2-c_route.py - From 1-hbnb_route.py. Added new Routes: '/' display "Hello HBNB!". '/hbnb' display "HBNB". /c/<text> display "C is <text>"
- 3-python_route.py - From 2-c_route.py. Added new Routes:
  - /' display "Hello HBNB!"
  - '/hbnb' display "HBNB"
  - /c/<text> display "C is <text>"
  - '/python/<text> - display "python is <text>". text is "cool" by default
