import httplib2
import sys
import json

import sys
import codecs
sys.stdout = codecs.getwriter('utf8')(sys.stdout)
sys.stderr = codecs.getwriter('utf8')(sys.stderr)

print "Running Endpoint Tester....\n"
address = raw_input("Please enter the address of the server you want to access, \n If left blank the connection will be set to 'http://localhost:5000':   ")
if address == '':
	address = 'http://localhost:5000'
#TEST ONE -- CREATE NEW RESTAURANTS
try:
	print "Test 1: Creating new Restaurants......"
	url = address + '/restaurants?location=Buenos+Aires+Argentina&mealType=Sushi'
	h = httplib2.Http()
	resp, result = h.request(url,'POST')
	if resp['status'] != '200':
		raise Exception('Received an unsuccessful status code of %s' % resp['status'])
	print json.loads(result)

	url = address + '/restaurants?location=Denver+Colorado&mealType=Soup'
	h = httplib2.Http()
	resp, result = h.request(url,'POST')
	if resp['status'] != '200':
		raise Exception('Received an unsuccessful status code of %s' % resp['status'])
	print json.loads(result)

	url = address + '/restaurants?location=Prague+Czech+Republic&mealType=Crepes'
	h = httplib2.Http()
	resp, result = h.request(url,'POST')
	if resp['status'] != '200':
		raise Exception('Received an unsuccessful status code of %s' % resp['status'])
	print json.loads(result).iteritems()

	url = address + '/restaurants?location=Shanghai+China&mealType=Sandwiches'
	h = httplib2.Http()
	resp, result = h.request(url,'POST')
	if resp['status'] != '200':
		raise Exception('Received an unsuccessful status code of %s' % resp['status'])
	print json.loads(result)

	url = address + '/restaurants?location=Nairobi+Kenya&mealType=Pizza'
	h = httplib2.Http()
	resp, result = h.request(url,'POST')
	if resp['status'] != '200':
		raise Exception('Received an unsuccessful status code of %s' % resp['status'])
	print json.loads(result)

except Exception as err:
	print "Test 1 FAILED: Could not add new restaurants"
	print err.args
	sys.exit()
else:
	print "Test 1 PASS: Succesfully Made all new restaurants"

#TEST TWO -- READ ALL RESTAURANTS
try:
	print "Attempting Test 2: Reading all Restaurants..."
	url = address + "/restaurants"
	h = httplib2.Http()
	resp, result = h.request(url,'GET')
	if resp['status'] != '200':
		raise Exception('Received an unsuccessful status code of %s' % resp['status'])
	all_result = json.loads(result)
	print result

except Exception as err:
	print "Test 2 FAILED: Could not retrieve restaurants from server"
	print err.args
	sys.exit()
else:
	print "Test 2 PASS: Succesfully read all restaurants"
#TEST THREE -- READ A SPECIFIC RESTAURANT
	try:
		print "Attempting Test 3: Reading the last created restaurant..."
		result = all_result
		restID = result['restaurants'][len(result['restaurants'])-1]['category']
		url = address + "/restaurants/%s" % restID
		print url
		h = httplib2.Http()
		resp, result = h.request(url,'GET')
		if resp['status'] != '200':
			raise Exception('Received an unsuccessful status code of %s' % resp['status'])
		print json.loads(result)

	except Exception as err:
		print "Test 3 FAILED: Could not retrieve restaurant from server"
		print err.args
		sys.exit()
	else:
		print "Test 3 PASS: Succesfully read last restaurant"

#TEST FOUR -- UPDATE A SPECIFIC RESTAURANT
	try:
		print "Attempting Test 4: Changing the name, image, and address of the first restaurant to Udacity..."
		result = all_result
		restID = result['restaurants'][0]['id']
		url = address + "/restaurants/%s?name=Udacity&address=2465+Latham+Street+Mountain+View+CA&image=https://media.glassdoor.com/l/70/82/fc/e8/students-first.jpg" % restID
		h = httplib2.Http()
		resp, result = h.request(url,'PUT')
		if resp['status'] != '200':
			raise Exception('Received an unsuccessful status code of %s' % resp['status'])
		print json.loads(result)

	except Exception as err:
		print "Test 4 FAILED: Could not update restaurant from server"
		print err.args
		sys.exit()
	else:
		print "Test 4 PASS: Succesfully updated first restaurant"

#TEST FIVE -- DELETE SECOND RESTARUANT 
try:
		print "Attempting Test 5: Deleteing the second restaurant from the server..."
		result = all_result
		restID = result['restaurants'][1]['id']
		url = address + "/restaurants/%s" % restID
		h = httplib2.Http()
		resp, result = h.request(url,'DELETE')
		if resp['status'] != '200':
			raise Exception('Received an unsuccessful status code of %s' % resp['status'])
		print result

except Exception as err:
	print "Test 5 FAILED: Could not delete restaurant from server"
	print err.args
	sys.exit()
else:
	print "Test 5 PASS: Succesfully updated first restaurant"
	print "ALL TESTS PASSED!"
