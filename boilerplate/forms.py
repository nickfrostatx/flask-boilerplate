from flask_wtf import Form
from wtforms import TextField, PasswordField
from wtforms.validators import DataRequired, Email

class LoginForm(Form):
    email = TextField('Email', [DataRequired(), Email()])
    password = PasswordField('Password', [DataRequired()])

class SignupForm(Form):
    email = TextField('Email', [DataRequired(), Email()])
    password = PasswordField('Password', [DataRequired()])
