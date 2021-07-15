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



if __name__ == '__main__':
    connect_to_db(app)
    app.run(host='0.0.0.0', debug=True)