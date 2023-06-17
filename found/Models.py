from found import db

'''In this file we defined the tables used in the database using the SQLALCHEMY toolkit which is an object-relational
for the python programming languege'''


# Define the users table with all the necessary fields.
class Users(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.String(length=30), nullable = False, unique = True)
    email = db.Column(db.String(length=50), nullable = False, unique = True)
    password_hash = db.Column(db.String(length=60), nullable = False)

# Define the songs table with all the necessary fields.
class Songs(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(length=60), nullable = False)
    singer = db.Column(db.String(length = 30), nullable=False)
    username = db.Column(db.String(length=30), nullable = False)
