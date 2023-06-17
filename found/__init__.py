from flask import Flask, request, render_template, session, flash
from flask_session import Session
from flask_sqlalchemy import SQLAlchemy
import os


'''In this file we initialised our project with all the necessary tools such asa the flask app and it configuration
the database cursor using the python toolkit SQLALCHEMY and the sessions.'''

app = Flask(__name__)

# configuring the session:
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configuring uploading folder:
app.config['UPLOAD_FOLDER'] = os.path.abspath(__name__) + "\\static\\files"
ALLOWED_EXTENSIONS = {'mp4', 'mov', 'avi', 'wmv', 'mkv'}

# configuring the database:
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///found.db'

#configuring the secret key:
app.config['SECRET_KEY'] = '7c10f77e58ef18ed3c7f74d3ex'

db = SQLAlchemy(app)
db.app = app
with app.app_context():
    db.create_all()

from found import routes
