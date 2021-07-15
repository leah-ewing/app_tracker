"""Script to seed database."""

import os
from random import choice, randint
from datetime import datetime

import crud
import model
import server

os.system('dropdb app_tracker')
os.system('createdb app_tracker')

model.connect_to_db(server.app)
model.db.create_all()

