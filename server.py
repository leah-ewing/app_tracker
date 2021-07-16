from flask import (Flask,render_template, request, flash, session, redirect)
from model import connect_to_db
import crud, requests
from jinja2 import StrictUndefined
from datetime import datetime

app = Flask(__name__)
app.secret_key = "dev"
app.jinja_env.undefined = StrictUndefined



@app.route('/')
def homepage():
    """Display the homepage"""

    return render_template("homepage.html")


@app.route('/login')
def login():
    """Displays the login page"""

    return render_template("login-page.html")


@app.route('/sign-up')
def signup():
    """Display sign-up page."""

    return render_template("sign-up-page.html")


@app.route('/login', methods = ["POST"])
def login_user():
    """Logs a user into their account."""

    email = request.form.get("email")
    password = request.form.get("password")
    fname = crud.get_user_fname(email)
    lname = crud.get_user_lname(email)
    valid_user = crud.login_user(email, password)
    
    if valid_user:
        session["current_user"] = email
        return render_template("user-profile.html", current_user = "current_user",
                                fname = fname, lname = lname)
    else:
        flash("Invalid login. Please try again.")
        return render_template("login-page.html")


@app.route('/create-account', methods = ["POST"])
def create_account():
    """Creates a new user account."""

    email = request.form.get("email")
    username = request.form.get("username")
    fname = request.form.get("fname")
    lname = request.form.get("lname")
    job_title = request.form.get("job_title")
    password = request.form.get("password")
    picture = request.form.get("picture")
    city = request.form.get("city")
    state = request.form.get("state")

    user_username = crud.get_username(username)
    user_email = crud.get_user_by_email(email)

    if user_username:
        flash("Username not available, please try again.")
        return redirect("/sign-up")
    elif user_email:
        flash("Profile already exists with that email. Please login or use a different email.")
        return redirect("/sign-up")
    else:
        crud.create_user(username, fname, lname, job_title, email, password, city, state, picture)
        session["current_user"] = email
        return render_template("user-profile.html", fname = fname, lname = lname)





if __name__ == '__main__':
    connect_to_db(app)
    app.run(host='0.0.0.0', debug=True)