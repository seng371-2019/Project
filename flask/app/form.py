
from datetime import datetime, date
from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, SubmitField
from wtforms.validators import DataRequired
from wtforms.fields.html5 import DateField

class SearchForm(FlaskForm):
    default_s = date(2000,01,01)
    default_e = date.today()
    print(default_s, default_e)
    dataset = StringField('Dataset', validators=[DataRequired()])
    startdate = DateField('Start date', format='%Y-%m-%d', default=default_s)
    enddate = DateField('End date', format='%Y-%m-%d', default=default_e)
    submit = SubmitField('Search')