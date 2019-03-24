from flask import render_template

from app import app
from app.form import SearchForm

@app.route('/')
@app.route('/index')
def home():
    return render_template('home.html', title='Home')

@app.route('/search')
def search():
    form = SearchForm()
    return render_template('search.html', title='Search',form=form)