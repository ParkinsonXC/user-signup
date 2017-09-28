from flask import Flask, request, redirect, render_template
import cgi
import os 


app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/", methods=['POST', 'GET'])
def index():

    if request.methods == "POST":
        username = request.form['username']
        password = request.form['password']
        verified_password = request.form['verified_password']


    return render_template('base.html', username=username, password=password, verified_password=verified_password)

@app.route("/welcome")
def welcome():

    username = request.form['username']
    return render_template('welcome.html', username=username)