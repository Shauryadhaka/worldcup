from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__, static_folder='static/public')

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///../data/db.worldcup.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)

import api.index
import api.matches
import api.clubs
import api.teams

import custom_filters

import models.country
import models.club
import models.position
import models.player