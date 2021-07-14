from flask import Flask, render_template
import requests

# Create a Flask Instance
app = Flask(__name__)

# Create a route decorator
@app.route('/')
# def index():
#     return "<h1>Hello World!</h1>"

###Filters
# safe
# capitalize
# lower
# upper
# title
# trim
# striptage


def index():
    first_name="Chris"
    stuff = "This is <strong>Bold Text</strong>"

    favorite_pizza = ["Pepperoni", "Cheese", "Mushrooms", 41]
    return render_template("index.html",first_name=first_name,stuff=stuff,favorite_pizza=favorite_pizza)

@app.route('/user/<name>')
def user(name):
    #    return "<h1>Hello You Rockin' Cool Dude -> {} !!!".format(name)
    return render_template("user.html",name=name)




if __name__ == '__main__':
    app.run()

