import httplib2
import json

def getGeocodeLocation(inputString):
	API_KEY ="AIzaSyAekotmI2nx2ZksgFOAQI_gkF5ja9tx4As"
	inputString = inputString.replace(" ","+")
	url = ('https://maps.googleapis.com/maps/api/geocode/json?address=%s&key=%s' %(inputString,API_KEY))

	h = httplib2.Http()
	response,content = h.request(url, 'GET')
	result = json.loads(content)
	lat = result['results'][0]['geometry']['location']['lat']
	lng = result['results'][0]['geometry']['location']['lng']
	return lat,lng

