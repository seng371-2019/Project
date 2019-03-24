
from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, SubmitField, DateField
from wtforms.validators import DataRequired

class SearchForm(FlaskForm):
    dataset = StringField('Dataset', validators=[DataRequired()])
    startdate = DateField('Start date', format='%Y-%m-%d', validators=[DataRequired()])
    enddate = DateField('End date', format='%Y-%m-%d', validators=[DataRequired()])
    submit = SubmitField('Search')