
from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, SubmitField, DateField
from wtforms.validators import DataRequired

class SearchForm(FlaskForm):
    dataset = StringField('Dataset', validators=[DataRequired()])
    startdate = DateField('Start date')
    enddate = DateField('End date')
    submit = SubmitField('Search')