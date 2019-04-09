from flask import flash, render_template, redirect, request, url_for

from app import app
from app.form import SearchForm
from app.mongodb import FromMongo


# Data used for testing. When the actual search results come back this will get replaced.
test_id = ["20170831_162740_ssc1d1", "20170831_172754_101c", "Houston-East-20170831-103f-100d-0f4f-RGB"]


@app.route('/')
def home():
    return redirect(url_for('search'))

@app.route('/search', methods=['GET', 'POST'])
def search():
    form = SearchForm()
    if form.validate_on_submit():
        # result = FromMongo(query, skip, cursor)
        flash('Searching  dataset "{}" between {} and {} dates, between {} and {} times, with cloud cover in range {} to {}'.format(form.dataset.data, form.startdate.data, form.enddate.data, form.starttime.data, form.endtime.data, form.mincloudcover.data, form.maxcloudcover.data))
        # replace test_id with returned id's
        return redirect(url_for('results'))
    return render_template('search.html', title='Search',form=form)

@app.route('/results')
def results():
    return render_template('results.html', title='Results')