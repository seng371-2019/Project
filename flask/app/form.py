
from datetime import datetime, date, time
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, FloatField, SubmitField
from wtforms.validators import DataRequired, NumberRange, Optional
from wtforms.fields.html5 import DateField, TimeField

class SearchForm(FlaskForm):
    default_start_date = date(2000,1,1)
    default_end_date = date.today()
    default_start_time = time(0,0,1)
    default_end_time = time(23,59,59)

    dataset = StringField('Dataset', validators=[DataRequired()])
    minlong = FloatField('Min Longitude', validators=[Optional()])
    maxlong = FloatField('Max Longitude', validators=[Optional()])
    minlat = FloatField('Min Latitude', validators=[Optional()])
    maxlat = FloatField('Max Latitude', validators=[Optional()])
    startdate = DateField('Start date', format='%Y-%m-%d', default=default_start_date)
    enddate = DateField('End date', format='%Y-%m-%d', default=default_end_date)
    starttime = TimeField('Start Time',default=default_start_time)
    endtime = TimeField('End Time',default=default_end_time)
    mincloudcover = IntegerField('Min Cloud cover', default=0, validators=[NumberRange(0,100)])
    maxcloudcover = IntegerField('Max Cloud cover', default=100, validators=[NumberRange(0,100)])

    submit = SubmitField('Search')