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

    if "current_user" in session:
        current_user = session["current_user"]
        return render_template("user-profile.html", current_user = "current_user")
    else:
        return render_template("homepage.html", current_user = None)


@app.route('/sign-up')
def signUp():
    """Display the sign-up page"""

    return render_template("sign-up-page.html")


@app.route('/login')
def login():
    """Display the login page"""

    if "current_user" in session:
        current_user = session["current_user"]
    else:
        return render_template("login-page.html", current_user = None)


@app.route('/profile-page')
def userProfile():
    """Displays a user's profile page"""

    if "current_user" in session:
        return render_template("user-profile.html", current_user = "current_user")
    else:
        return redirect('/')


@app.route('/login-user', methods = ["POST"])
def loginUser():
    """Login user and redirect them to their profile"""

    email = request.form.get("email")
    password = request.form.get("password")
    valid_user = crud.login_user(email, password)

    if valid_user:
        session["current_user"] = email
        flash("Welcome back!")
        # return render_template("user-profile.html", current_user = "current_user")
        return redirect('/profile-page')
    else:
        flash("Invalid login, please try again")
        return redirect('/')


@app.route('/logout', methods = ["POST"])
def logout():
    """Logout user and redirect them to the homepage."""

    if "current_user" in session:
        session["current_user"] = None
        session.pop("current_user")
        flash("You have been signed out!")
        return render_template("homepage.html", current_user = None)
    else:
        return redirect('/')







if __name__ == '__main__':
    connect_to_db(app)
    app.run(host='0.0.0.0', debug=True)