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
        #return redirect("/?username_error=" + username_error)

    elif len(username) > 20:
        username = ""
        username_error = "This username is too long."
        #return redirect("/?username_error=" + username_error)

    elif ' ' in username:
        username = ""
        username_error = "Your username cannot have a space."
        #return redirect("/?username_error=" + username_error)

        
    #PASSWORD CHECK
    if len(password) <= 3:
        password = ""
        verified_password = ""
        password_error = "This password is too short."
        #return redirect("/?password_error=" + password_error)

    elif len(password) > 20:
        password = ""
        verified_password = ""
        password_error = "This password is too long."
        #return redirect("/?password_error=" + password_error)

    elif ' ' in password:
        password = ""
        verified_password = ""
        password_error = "Your password cannot have a space."
        #return redirect("/?password_error=" + password_error)

    #VERIFY CHECK
    if password != verified_password:
        password = ""
        verified_password = ""
        verified_error = "Your passwords don't match."
        #return redirect("/?verified_error=" + verified_error)

    #EMAIL IS OPTIONAL, SO WE HAVE TO SEE IF THEY FILLED IN THE BOX OR NOT BY CHECKING LENGTH
    if len(email) != 0:

        #EMAIL CHECK (OPTIONAL)
        if email.count('@') != 1 or email.count('@') > 1:
            email = ""
            email_error = "Invalid email."
            #return redirect("/?email_error=" + email_error)

        elif email.count('.') != 1 or email.count('.') > 1:
            email = ""
            email_error = "Invalid email."
            #return redirect("/?email_error=" + email_error)

        elif len(email) <= 3 or len(email) > 20:
            email = ""
            email_error = "Invalid email."
    #SHOULD NO ERROR OCCUR:
    if not username_error and not password_error and not verified_error and not email_error:
        return render_template("welcome.html", username=username)

    else:
         return render_template("signup.html",
        username=username,
        username_error=username_error,
        password_error=password_error,
        verified_error=verified_error,
        email_error=email_error)

app.run()