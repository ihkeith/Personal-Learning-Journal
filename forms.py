from flask_wtf import FlaskForm
from wtforms import (StringField, PasswordField, BooleanField, TextField,
                    DateField, IntegerField)
from wtforms.validators import (DataRequired, Regexp, ValidationError, Email,
                               Length, EqualTo)


from models import Entry, User

def email_exists(form, field):
    if User.select().where(User.email == field.data).exists():
        raise ValidationError('User with that email aready exists.')


def is_integer(form, field):
    if not int(field.data):
        raise ValidationError('Time spent must be an integer')

class RegisterForm(FlaskForm):
    email = StringField(
        'Email',
        validators=[
            DataRequired(),
            Email(),
            email_exists
        ]
    )
    password = PasswordField(
        'Password',
        validators=[
            DataRequired(),
            Length(min=8),
            EqualTo('password2', message='Passwords must match')
        ]
    )
    password2 = PasswordField(
        'Confirm Password',
        validators=[
            DataRequired()
        ]
    )


class LoginForm(FlaskForm):
    email = StringField(
        'Email',
        validators=[
            DataRequired(),
        ]
    )
    password = PasswordField(
        'Password',
        validators=[
            DataRequired(),
        ]
    )


class NewEntry(FlaskForm):
    title = StringField(
        'Title',
        validators=[
            DataRequired()
        ]
    )
    date = DateField(
        'Date',
        validators=[
            DataRequired(),
        ]
    )
    time_spent = IntegerField(
        'Time Spent',
        validators=[
            DataRequired(),
            is_integer
        ]
    )
    learned = TextField(
        'What I Learned',
        validators=[
            DataRequired()
        ]
    )
    resources = TextField(
        'Resources to Remember',
        validators=[
            DataRequired()
        ]
    )