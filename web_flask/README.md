## 0x04. AirBnB clone - Web framework

This project is about udnerstanding Web Framework.
- How to build a web framework with Flask.
- What is route and template.
- How to create an HTML response in Flask by using a template
- How to create a dynamic template (loops, conditions...)
- How to display in HTML data from a MySQL database

Install Flask
```pip3 install flash```

## Tasks:
- 0-hello_route.py - script that starts a Flask web application. Web application must be listening on 0.0.0.0, port 5000. Routes '/' display "Hello HBNB!".
- 1-hbnb_route.py - From 0-hello_route.py. Added new Routes: '/' display "Hello HBNB!". '/hbnb' display "HBNB"
- 2-c_route.py - From 1-hbnb_route.py. Added new Routes: '/' display "Hello HBNB!". '/hbnb' display "HBNB". /c/<text> display "C is <text>"
- 3-python_route.py - From 2-c_route.py. Added new Routes:
  - /' display "Hello HBNB!"
  - '/hbnb' display "HBNB"
  - /c/<text> display "C is <text>"
  - '/python/<text> - display "python is <text>". text is "cool" by default