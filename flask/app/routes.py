from flask import flash, render_template, redirect, request, url_for
import pymongo

from app import app
from app.form import SearchForm
from app.mongodb import FromMongo

def mincloudcover(collection, min):
	for item in collection:
		if item["properties"]["eo:cloud_cover"] < min:
			collection.remove(item)
	return collection
	
def maxcloudcover(collection, max):
	for item in collection:
		if item["properties"]["eo:cloud_cover"] > max:
			collection.remove(item)
	return collection		
	
def filter(form):
	client = pymongo.MongoClient("mongodb+srv://[USERNAME]:[PASSWORD]@testing-jcwfi.mongodb.net/test?retryWrites=true")
	my_database = client.testing.testjson
	my_collection = my_database
	list = my_collection.find()
	my_cursor = []
	for item in list:
		my_cursor.append(item)
	
	my_cursor = mincloudcover(my_cursor, form.mincloudcover.data)
	my_cursor = maxcloudcover(my_cursor, form.maxcloudcover.data)
	
	return my_cursor
	
@app.route('/')
def home():
    return redirect(url_for('search'))

@app.route('/search', methods=['GET', 'POST'])
def search():
	form = SearchForm()
	if form.validate_on_submit():
		# data = FromMongo(query, skip, cursor)
		results = filter(form)
		flash('Searching  dataset "{}" between {} and {} dates, between {} and {} times, with cloud cover in range {} to {}'.format(form.dataset.data, form.startdate.data, form.enddate.data, form.starttime.data, form.endtime.data, form.mincloudcover.data, form.maxcloudcover.data))
		for item in results:
			flash(item["id"])
		return redirect(url_for('results'))
	return render_template('search.html', title='Search',form=form)

@app.route('/results')
def results():
	return render_template('results.html', title='Results')