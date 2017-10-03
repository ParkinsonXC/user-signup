from flask import Flask, request, redirect, render_template
import cgi
import os 


app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/")
def display_signup_form():
    return render_template("signup.html")

@app.route('/', methods=['POST'])
def validate_input():
    username = request.form['username']
    password = request.form['password']
    verified_password = request.form['verified_password']
    email = request.form['email']

    username_error = ""
    password_error = ""
    verified_error = ""
    email_error = ""

    #USERNAME CHECK
    if len(username) <= 3:
        username = ""
        username_error = "This username is too short."


    elif len(username) > 20:
        username = ""
        username_error = "This username is too long."

    elif ' ' in username:
        username = ""
        username_error = "Your username cannot have a space."


        
    #PASSWORD CHECK
    if len(password) <= 3:
        password = ""
        verified_password = ""
        password_error = "This password is too short."

    elif len(password) > 20:
        password = ""
        verified_password = ""
        password_error = "This password is too long."

    elif ' ' in password:
        password = ""
        verified_password = ""
        password_error = "Your password cannot have a space."


    #VERIFY CHECK
    if password != verified_password:
        password = ""
        verified_password = ""
        verified_error = "Your passwords don't match."


    #EMAIL IS OPTIONAL, SO WE HAVE TO SEE IF THEY FILLED IN THE BOX OR NOT BY CHECKING LENGTH
    if len(email) != 0:

        #EMAIL CHECK (OPTIONAL)
        if email.count('@') != 1 or email.count('@') > 1:
            email = ""
            email_error = "Invalid email."


        elif email.count('.') != 1 or email.count('.') > 1:
            email = ""
            email_error = "Invalid email."
            

        elif len(email) <= 3 or len(email) > 20:
            email = ""
            email_error = "Invalid email."
    #SHOULD NO ERROR OCCUR:
    if not username_error and not password_error and not verified_error and not email_error:
        return render_template("welcome.html", username=username)

    else:
         return render_template("signup.html",
        username=username,
        email=email,
        username_error=username_error,
        password_error=password_error,
        verified_error=verified_error,
        email_error=email_error)

app.run()