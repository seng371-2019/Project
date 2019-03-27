import os
import json
import sys

def newdir(newdirectory): #Find json files and call searchjson() on 
	current = os.getcwd() #them. Then recursivly searches sub direcories.
	os.chdir(newdirectory)
	for item in os.listdir():
		if os.path.splitext(item)[1] == '.json':
			if searchjson(item):
				print(os.getcwd() + item)
		elif os.path.splitext(item)[1] == '':
			newdir(item)
	os.chdir(current)		
	return newdirectory
	
def searchjson(file): #Loads json file and tests to see if it matches criteria
	result = False    #Currently hard coded to search for two set IDs
	with open(file) as json_file:  
		data = json.load(json_file)

	try:	#Try block is used when the property being search for isn't in every json
			#Can later be changed to verify before searching using list of JSON keys
		if data[sys.argv[1]] == sys.argv[2]:
			result = True
	except:
		print("Could not find selected key in this JSON dictionary")
	return result

	
	
if len(sys.argv) != 3:   #Prevents user from incorrectly formating arguments
	print('Please use this format: search.py "Property Key" "Property Value"')
	print('e.g. search.py id 20170831_172754_101c')
	exit()
	
print('Searching for:') 
print('Property: ' + sys.argv[1] + ' & Value: ' + sys.argv[2])
newdir('disasters') #Begin search for json at this directory