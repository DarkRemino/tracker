from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField
from wtforms.validators import InputRequired, Length, EqualTo, Regexp, Email


# I'm not including any submit fields as they can only be rendered into <input> tags and I want to use buttons instead
class LoginForm(FlaskForm):
    email = StringField('Email', validators=[InputRequired()])
    password = PasswordField('Password', validators=[InputRequired()])
    remember_me = BooleanField('Keep me logged in')


class RegistrationForm(FlaskForm):
    email = StringField('Email', validators=[InputRequired()])
    password1 = PasswordField('Password', validators=[InputRequired()])
    password2 = PasswordField('Repeat the password', validators=[InputRequired(), EqualTo('password', message='Passwords must match')])
    tos = BooleanField('Terms of service')
    newsletter = BooleanField('Subscribe to our newsletter!')