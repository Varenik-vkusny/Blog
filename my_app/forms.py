from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, EmailField, BooleanField, validators
from wtforms.validators import Email

class RegistrationForm(FlaskForm):
    username = StringField('Username', [validators.DataRequired(), validators.length(min=4, max=25)])
    email = EmailField('Email', [validators.DataRequired(), Email()])
    password = PasswordField('Password', [validators.DataRequired(), validators.length(min=6, max=35)], equal_to='confirm', message='Passwords must match')
    confirm = PasswordField('Confirm Password', [validators.DataRequired()])

class LoginForm(FlaskForm):
    email = StringField('Email', [validators.DataRequired(), Email()])
    password = PasswordField('Password', [validators.DataRequired(), validators.length(min=6, max=35)])
    remember = BooleanField('Remember Me')