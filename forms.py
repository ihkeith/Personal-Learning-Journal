from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, DateField, IntegerField
from wtforms.validators import DataRequired

# add custom validator to ensure that INT is intered into time spent

class NewEntry(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    date = DateField('Date', validators=[DataRequired()])
    time_spent = IntegerField('Time Spent', validators=[DataRequired()])
    learned = TextAreaField('What I Learned', validators=[DataRequired()])
    resources = TextAreaField('Resources to Remember', validators=[DataRequired()])


class EditEntry(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    date = DateField('Date', validators=[DataRequired()])
    time_spent = IntegerField('Time Spent', validators=[DataRequired()])
    learned = TextAreaField('What I Learned', validators=[DataRequired()])
    resources = TextAreaField('Resources to Remember', validators=[DataRequired()])