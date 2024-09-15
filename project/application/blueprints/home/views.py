from application.blueprints.home import home
from flask import render_template

@home.route('/')
def welcome_page():
    print("Hello")
    return render_template("home.html")