from flask import flash, render_template, redirect, request, url_for

from app import app
from app.form import SearchForm

@app.route('/')
@app.route('/search', methods=['GET', 'POST'])
def search():
    form = SearchForm()
    if form.validate_on_submit():
        flash('Searching  dataset "{}" between {} and {} dates, between {} and {} times, with cloud cover in range {} to {}'.format(form.dataset.data, form.startdate.data, form.enddate.data, form.starttime.data, form.endtime.data, form.mincloudcover.data, form.maxcloudcover.data))
        return redirect(url_for('results'))
    return render_template('search.html', title='Search',form=form)

@app.route('/results')
def results():
    return render_template('results.html', title='Results')