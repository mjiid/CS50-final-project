from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, FileField
from wtforms.validators import Length, DataRequired, Email, EqualTo


''' In this file we created the forms using the wtforms python library in order to avoid CSRF attacks,
and also because it supports data validation.'''


# Create the register form
class RegisterForm(FlaskForm):
    username = StringField(label='Username', validators = [Length(min = 4,max = 25), DataRequired()])
    email = StringField('Email', validators=[Email(), DataRequired()])
    password1 = PasswordField('Password', validators=[DataRequired(), Length(min=6)])
    password2 = PasswordField('Confirmation', validators=[DataRequired(), EqualTo('password1')] )
    submit = SubmitField(label='Submit')

# Create the login form
class LoginForm(FlaskForm):
    username = StringField(label="username", validators = [DataRequired()])
    password = PasswordField(label="password", validators = [DataRequired()])
    submit = SubmitField(label="Submit")

# Create the upload file form
class Uploadfile(FlaskForm):
    file = FileField("File")
    submit = SubmitField("Upload file")
