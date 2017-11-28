from urllib import urlencode
from httplib2 import Http
import json
import sys
import base64


print "Running Endpoint Tester....\n"
address = raw_input("Please enter the address of the server you want to access, \n If left blank the connection will be set to 'http://localhost:5000':   ")
if address == '':
	address = 'http://localhost:5000'

#TEST 1: TRY TO REGISTER A NEW USER 
try:
	h = Http()
	url = address + '/users'
	data = dict(username="Peter", password="Pan")
	data = json.dumps(data)
	resp, content = h.request(url,'POST', body = data, headers = {"Content-Type": "application/json"})
	if resp['status'] != '201' and resp['status'] != '200':
 		raise Exception('Received an unsuccessful status code of %s' % resp['status'])

except Exception as err:
	print "Test 1 FAILED: Could not make a new user"
	print err.args
	sys.exit()
else:
	print "Test 1 PASS: Succesfully made a new user"

#TEST 2: OBTAIN A TOKEN
try:
	h = Http() 
	h.add_credentials('Peter','Pan')
	url = address + '/token'
	resp, content = h.request(url,'GET' , headers = {"Content-Type" : "application/json"})
	print resp
	if resp['status'] != '200':
		raise Exception('Received an unsuccessful status code of %s' % resp['status'])
	new_content = json.loads(content)
	if not new_content['token']:
		raise Exception('No Token Received!')
	token = new_content['token']
	print "received token: %s" % token
except Exception as err:
	print "Test 2 FAILED: Could not exchange user credentials for a token"
	print err.args
	sys.exit()
else:
	print "Test 2 PASS: Succesfully obtained token! "

#TEST 3: TRY TO ADD PRODUCS TO DATABASE

try:
	h = Http()
	h.add_credentials(token,'blank')
	url = address + '/products'
	data = dict(name = "apple", category = "fruit", price= "$.99")
	resp, content = h.request(url,'POST', body = json.dumps(data), headers = {"Content-Type" : "application/json"})
	if resp['status'] != '200':
		raise Exception('Received an unsuccessful status code of %s' % resp['status'])
except Exception as err:
	print "Test 3 FAILED: Could not add new products"
	print err.args
	sys.exit()
else:
	print "Test 3 PASS: Succesfully added new products"


#TEST 4: TRY ACCESSING ENDPOINT WITH AN INVALID TOKEN
try:
	h = Http()
	h.add_credentials('wrong_token','blank')
	url = address + '/products'
	resp, result = h.request(url,'GET', headers = {"Content-Type" : "application/json"})
	if resp['status'] == '200':
		raise Exception('Received an unsuccessful status code of %s' % resp['status'])		
except Exception as err:
	print "Test 5 FAILED"
	print err.args
	sys.exit()
else:
	print "Test 5 PASS: App checks against invalid credentials"


#TEST 5: TRY TO VIEW ALL PRODUCTS IN DATABASE 

try:
	h = Http()
	h.add_credentials(token,'blank')
	url = address + '/products'
	resp, result = h.request(url,'GET', headers = {"Content-Type" : "application/json"})
	if resp['status'] != '200':
		raise Exception('Received an unsuccessful status code of %s' % resp['status'])
	all_result = json.loads(result)
	print result			
except Exception as err:
	print "Test 5 FAILED: Could not view products"
	print err.args
	sys.exit()
else:
	print "Test 5 PASS: Succesfully viewed all products"


#TEST 6: TRY TO VIEW A SPECIFIC CATEGORY OF PRODUCTS
try:
	print "Attempting Test 6: Reading the last added products category..."
	result = all_result
	prodCat = result['products'][len(result['products'])-1]['category']
	url = address + "/products/%s" % prodCat
	print url
	h = Http()
	h.add_credentials(token,'blank')
	resp, result = h.request(url,'GET', headers = {"Content-Type" : "application/json"})
	if resp['status'] != '200':
		raise Exception('Received an unsuccessful status code of %s' % resp['status'])
	print json.loads(result)

except Exception as err:
	print "Test 6 FAILED: Could not retrieve product category from server"
	print err.args
	sys.exit()
else:
	print "Test 6 PASS: Succesfully viewed last product category"
	print "ALL TESTS PASSED!"