from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,BooleanField,SubmitField
from wtforms.validators import InputRequired,Email,EqualTo
from ..models import User
from wtforms import ValidationError



class RegistrationForm(FlaskForm):

    email = StringField('Your Email Address')
    username = StringField('Enter your username')
    password = PasswordField('Password')
    EqualTo('password_confirm')
    password_confirm = PasswordField('Confirm Passwords')
    submit = SubmitField('Sign Up')

    

class LoginForm(FlaskForm):
    email = StringField('Your Email Address')
    password = PasswordField('Password')
    remember = BooleanField('Remember me')
    submit = SubmitField('Sign In')


