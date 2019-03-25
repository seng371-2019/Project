from flask import flash, render_template, redirect, request, url_for

from app import app
from app.form import SearchForm

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', title='Home')

@app.route('/search', methods=['GET', 'POST'])
def search():
    form = SearchForm()
    if form.validate_on_submit():
        flash('Searching  dataset {} between {} and {}'.format(form.dataset.data, form.startdate.data, form.enddate.data))
        return redirect(url_for('home'))
    return render_template('search.html', title='Search',form=form)