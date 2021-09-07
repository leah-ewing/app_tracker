from flask import (Flask,render_template, request, flash, session, redirect)
from model import connect_to_db
import crud, requests
from jinja2 import StrictUndefined
from datetime import datetime

app = Flask(__name__)
app.secret_key = "dev"
app.jinja_env.undefined = StrictUndefined



@app.route('/', methods = ["POST"])
def homepage():
    """Display the homepage"""

    return render_template("homepage.html")


@app.route('/sign-up')
def signUp():
    """Display the sign-up page"""

    return render_template("sign-up-page.html")


@app.route('/login')
def login():
    """Display the login page"""

    return render_template("login-page.html")

@app.route('/user-profile', methods = ["POST"])
def loginUser():
    """Login user and redirect them to their profile"""

    email = request.form.get("email")
    password = request.form.get("password")
    valid_user = crud.login_user(email, password)

    if valid_user:
        session["current_user"] = email
        return render_template("user-profile")
    else:
        flash("Invalid login, please try again")
        return redirect('/')









if __name__ == '__main__':
    connect_to_db(app)
    app.run(host='0.0.0.0', debug=True)