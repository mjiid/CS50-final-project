from found import app, db, session, Session, flash, ALLOWED_EXTENSIONS
from flask import render_template, request, redirect, url_for
from found.Models import Users, Songs
from found.forms import RegisterForm, LoginForm, Uploadfile
import bcrypt, os
from werkzeug.utils import secure_filename
from found.functions import allowed_file, extract_audio, save_audio
from found.song_recognition import recognize


'''In this file we defined each route separatly with its own functionalities, we also managed the sessions
so the user can be remembered in case he didn't logout of the website, and we have also stored the data 
not only about the registered users, but also the identified songs'''

# Create all the tables before the first user request arrives.
with app.app_context():
    db.create_all()

# index page/route.
@app.route("/", methods=["GET", "POST"])
def index():
    return render_template("index.html")

# the home page/route, in case the user has already logged in.
@app.route("/home", methods = ["GET", "POST"])
def home():
    if "name" not in session.keys():
        return redirect(url_for("index"))
    else:
        form = Uploadfile()

    return render_template("home.html", form = form)

# uploading the file.
@app.route("/upload", methods= ["GET", "POST"])
def upload():
    form = Uploadfile()

    # Uploading the video:
    if form.validate_on_submit():

        # Saving the video in a file and extract the audio:
        allowed = False

        # The user didn't input any file:
        if form.file.data.filename == "":
            return redirect(url_for('home'))

        # Check if the format of the file is allowed
        if allowed_file(form.file.data.filename):
            filename = secure_filename(form.file.data.filename)
            extract_audio(form, filename)
            allowed = True
            
        # Check if the file is an mp3 file:
        if '.mp3' in form.file.data.filename:
            allowed = True
            save_audio(form, form.file.data.filename)

        # Recognize the song from the file:
        if recognize(form.file.data.filename) != False and allowed:
            artist = recognize(form.file.data.filename)[1]
            title = recognize(form.file.data.filename)[2]
            username = session['name']
            identified_song = Songs(name = title, singer = artist, username = username)
            db.session.add(identified_song)
            db.session.commit()

            return redirect(recognize(form.file.data.filename)[0])
        else:
                return render_template("Song not found Sorry!")

    return render_template("home.html", form = form)


# This is the register page:
@app.route("/register", methods = ["GET", "POST"])
def register():
    if "name" in session.keys():
        return redirect(url_for("home"))
    else:
        form = RegisterForm()

        if form.validate_on_submit():

            # Hash the password:
            bytePwd = form.password1.data.encode('utf-8')
            salt = bcrypt.gensalt()
            pwd_hash = bcrypt.hashpw(bytePwd, salt)

            # Check if username or email is already used
            existing_usernames = Users.query.filter_by(username = form.username.data).all()
            existing_emails = Users.query.filter_by(email = form.email.data).all()
            if len(existing_usernames) > 0:
                flash('Username already in use', 'error')
                return redirect(url_for('register'))
            if len(existing_emails) > 0:
                flash('Email already in use', 'error')
                return redirect(url_for('register'))

            # Store the data:
            user_to_create = Users(username = form.username.data,
            email = form.email.data,
            password_hash = pwd_hash)

            db.session.add(user_to_create)
            db.session.commit()

            # record the username:
            session['name'] = form.username.data

            return redirect(url_for('home'))
        
        if form.errors != {}:
            for err_msg in form.errors.values:
                flash(err_msg)

    return render_template('register.html', form = form)


# This is the login page.
@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if "name" in session.keys():
        return redirect(url_for('home'))

    if form.validate_on_submit():
        usrname = form.username.data
        password = form.password.data
        
        if (Users.query.filter_by(username = usrname).first() is not None):
            user = Users.query.filter_by(username = usrname).first()
            pwd_hash = user.password_hash
            password = password.encode("utf-8")

            if (bcrypt.checkpw(password, pwd_hash)):
                session['name'] = usrname
                return render_template("home.html", form = Uploadfile())
            else:
                flash('Invalid password provided', 'error')
                return redirect(url_for('login'))
        else:
            flash('Invalid username provided', 'error')
            return redirect(url_for("login"))
        

    return render_template("login.html", form = form)


# T is the page of the identified song.
@app.route("/songs")
def songs():
    songs = Songs.query.filter_by(username = session['name']).all()
    return render_template('songs.html', songs = songs)


# This is the logout route.
@app.route("/logout")
def logout():
    del session["name"]
    return redirect("/")

