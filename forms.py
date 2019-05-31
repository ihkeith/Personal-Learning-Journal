from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, DateField, IntegerField
from wtforms.validators import DataRequired, ValidationError

# add custom validator to ensure that INT is intered into time spent
def is_number(form, field):
    if not int(field.data):
        raise ValidationError("Please enter numbers only.")


class NewEntry(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    date = DateField('Date', validators=[DataRequired()])
    time_spent = IntegerField(
        'Time Spent',
        validators=[DataRequired(), is_number]
    )
    learned = TextAreaField('What I Learned', validators=[DataRequired()])
    resources = TextAreaField('Resources to Remember', validators=[DataRequired()])


class EditEntry(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    date = DateField('Date', validators=[DataRequired()])
    time_spent = IntegerField(
        'Time Spent',
        validators=[DataRequired(), is_number]
    )
    learned = TextAreaField('What I Learned', validators=[DataRequired()])
    resources = TextAreaField('Resources to Remember', validators=[DataRequired()])