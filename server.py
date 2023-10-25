# Python Flask file to handle the backend
# Name - Indrajeet Mondal; Date = 25th October 2023
# SourceCode

from flask import Flask, render_template

app = Flask(__name__)


# A normal routing
@app.route("/")
def index():
    return render_template("./index.html")

# A normal routing
@app.route("/about")
def about():
    return render_template("./about.html")

# Creating a blog routing
@app.route("/blog")
def hello_bloggers():
    return "<h1><center>Hello Bloggers!!</center></h1>"
