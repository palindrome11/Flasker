from flask import Flask, render_template
import requests

# Create a Flask Instance
app = Flask(__name__)

# Create a route decorator
@app.route('/')
def index():
    return "<h1>Hello World!</h1>"

@app.route('/user/<name>')
def user(name):
    return "<h1>Hello {} !!!".format(name)



app.run()

