"""Script to seed database."""

import os
from random import choice, randint
from datetime import datetime

import crud
import model
import server

os.system('dropdb tracker')
os.system('createdb tracker')

model.connect_to_db(server.app)
model.db.create_all()

"""Creator login."""
c_username = "leahnidus"
c_fname = "Leah"
c_lname = "Ewing"
c_job_title = "Software Engineer"
c_email = "leah@test.test"
c_password = "test"
c_city = "Nashville"
c_state = "TN"
c_picture = "https://cdn.dribbble.com/users/26684/screenshots/10877696/media/d3d1d16d38cd66dfa315ffd89bb58536.png?compress=1&resize=400x300"

creator = crud.create_user(c_username, c_fname, c_lname, c_job_title, c_email, c_password, c_city, c_state, c_picture)
