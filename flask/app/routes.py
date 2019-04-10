from flask import flash, render_template, redirect, request, url_for
import pymongo
from datetime import datetime

from app import app
from app.form import SearchForm
from app.mongodb import FromMongo

#list used to hold id's of query results
result_id = []

#converts a string to datetime
def convertDateTime(str):
	dt = datetime.strptime(str, '%Y-%m-%dT%H:%M:%S.%fz')
	return dt

#Querying min cloud cover
def mincloudcover(collection, min):
	toRemove = []
	for item in collection:
		if item["properties"]["eo:cloud_cover"] < min:
			toRemove.append(item)
	for i in toRemove:
		collection.remove(i)
	return collection

#Querying max cloud cover	
def maxcloudcover(collection, max):
	toRemove = []
	for item in collection:
		if item["properties"]["eo:cloud_cover"] > max:
			toRemove.append(item)
	for i in toRemove:
		collection.remove(i)
	return collection

#Querying min time
def mintime(collection, min):
	toRemove = []
	for item in collection:
		if convertDateTime(item["properties"]["datetime"]).time() < min:
			toRemove.append(item)
	for i in toRemove:
		collection.remove(i)
	return collection

#Querying max time	
def maxtime(collection, max):
	toRemove = []
	for item in collection:
		if convertDateTime(item["properties"]["datetime"]).time() > max:
			toRemove.append(item)
	for i in toRemove:
		collection.remove(i)
	return collection

#Querying min date
def mindate(collection, min):
	toRemove = []
	for item in collection:
		if convertDateTime(item["properties"]["datetime"]).date() < min:
			toRemove.append(item)
	for i in toRemove:
		collection.remove(i)
	return collection

#Querying max cloud cover	
def maxdate(collection, max):
	toRemove = []
	for item in collection:
		if convertDateTime(item["properties"]["datetime"]).date() > max:
			toRemove.append(item)
	for i in toRemove:
		collection.remove(i)
	return collection	
	
def filter(form):
	client = pymongo.MongoClient("mongodb+srv://teamname:teamname@project2-stacdata-osuhm.gcp.mongodb.net/test?retryWrites=true")
	my_database = client.project_2.stac_data
	my_collection = my_database
	list = my_collection.find()
	my_cursor = []
	for item in list:
		my_cursor.append(item)
	#query all items in the collection
	my_cursor = mincloudcover(my_cursor, form.mincloudcover.data)
	my_cursor = maxcloudcover(my_cursor, form.maxcloudcover.data)
	my_cursor = mintime(my_cursor, form.starttime.data)
	my_cursor = maxtime(my_cursor, form.endtime.data)
	my_cursor = mindate(my_cursor, form.startdate.data)
	my_cursor = maxdate(my_cursor, form.enddate.data)
	#return cursor with remaining jsons
	return my_cursor
	
@app.route('/')
def home():
    return redirect(url_for('search'))

@app.route('/search', methods=['GET', 'POST'])
def search():
	form = SearchForm()
	if form.validate_on_submit():
		#get query results
		results = filter(form)

		#flash('Searching  dataset "{}" between {} and {} dates, between {} and {} times, with cloud cover in range {} to {}'.format(form.dataset.data, form.startdate.data, form.enddate.data, form.starttime.data, form.endtime.data, form.mincloudcover.data, form.maxcloudcover.data))
		for item in results:
			result_id.append(item["id"])
		return redirect(url_for('results'))
	return render_template('search.html', title='Search',form=form)

@app.route('/results')
def results():
	return render_template('results.html', title='Results', results = result_id)