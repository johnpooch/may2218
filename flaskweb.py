
# Web Server Gateway Interface (WSGI) is a simple calling convention for web servers to forward requests to web applications or frameworks written in the Python programming language.

# The GET method requests a representation of the specified resource. Requests using GET should only retrieve data.
# The POST method is used to submit an entity to the specified resource, often causing a change in state or side effects on the server.

# Flask configures the Jinja2 template engine for you automatically.
#

from flask import Flask, request, render_template # First import the Flask class. An instance of this class will be our WSGI application. 

# To render a template you can use the render_template() method. All you have to do is provide the name of the template and the variables you want to pass to the template engine as keyword arguments.

import os # The OS module in Python provides a way of using operating system dependent functionality. 
import datetime

app = Flask(__name__) # Then create an instance of this class. The first argument is the name of the application’s module or package. If you are using a single module (as in this example), you should use __name__.

@app.route("/") # use the route() decorator to tell Flask what URL should trigger the function.
def show_hi():
    return render_template("index.html")
    
@app.route("/search", methods = ['POST'])
def do_search():
    # # Getting arguments from a GET quesry string
    # make = request.args.get('make')
    # model = request.args.get('model')
    
    # Getting arguments from a POST form
    make = request.form.get('make')
    model = request.form.get('model')
    
    