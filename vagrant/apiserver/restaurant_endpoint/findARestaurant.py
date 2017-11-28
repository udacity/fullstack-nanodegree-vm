from geocode import getGeocodeLocation
import json
import httplib2

import sys
import codecs
sys.stdout = codecs.getwriter('utf8')(sys.stdout)
sys.stderr = codecs.getwriter('utf8')(sys.stderr)

foursquare_client_id = "URF15OGCPJ1TLULVBABNIUQ0Z4DG0V0MG4M30CXCZHJCGTES"
foursquare_client_secret = "14SK5TBI4RESQ4C4NWDQOYT03L3K0YE5025BMRPEYTEOHQJN"


def findARestaurant(mealType,location):
  #1. Use getGeocodeLocation to get the latitude and longitude coordinates of the location string.
  lat,lng = getGeocodeLocation(location)
  
  #2.  Use foursquare API to find a nearby restaurant with the latitude, longitude, and mealType strings.
  #HINT: format for url will be something like https://api.foursquare.com/v2/venues/search?client_id=CLIENT_ID&client_secret=CLIENT_SECRET&v=20130815&ll=40.7,-74&query=sushi
  url = "https://api.foursquare.com/v2/venues/search?client_id=%s&client_secret=%s&v=20161016&ll=%s,%s&query=%s" % (foursquare_client_id,foursquare_client_secret,lat,lng,mealType)
  h = httplib2.Http()
  resp,content = h.request(url, 'GET')
  result = json.loads(content)
  #3. Grab the first restaurant
  if result['response']['venues']:
    firstRestaurant = result['response']['venues'][0]  
    venue_address =""
    venue_name = firstRestaurant['name']
    addresses = firstRestaurant['location']['formattedAddress']
    for addr in addresses:
      venue_address += addr + " "    
    #4. Get a  300x300 picture of the restaurant using the venue_id (you can change this by altering the 300x300 value in the URL or replacing it with 'orginal' to get the original picture
    venue_id = firstRestaurant['id']
    #5. Grab the first image
    venue_photos_url = "https://api.foursquare.com/v2/venues/%s/photos?client_id=%s&client_secret=%s&v=20131016&group=venue" % (venue_id,foursquare_client_id,foursquare_client_secret)
    h1 = httplib2.Http()
    photos_resp,photos_content = h1.request(venue_photos_url, 'GET')
    photos_result = json.loads(photos_content)  
    try:
      venue_photo = photos_result["response"]["photos"]["items"][0]
      url_prefix = venue_photo['prefix']
      size = "300x300"
      url_suffix = venue_photo['suffix']
      photo_url = url_prefix + size + url_suffix
    #6. If no image is available, insert default a image url
    except Exception as e:
      photo_url = "http://via.placeholder.com/300x300"

    #7. Return a dictionary containing the restaurant name, address, and image url  
    output = dict(name=venue_name,address=venue_address,image_url=photo_url)
    print "Restaurant Name: %s" % json.dumps(venue_name)
    print "Restaurant Address: %s`" % json.dumps(venue_address)
    print "Image: %s" % photo_url
    return output
  else:
    print "No Restaurant found for the location : %s"  % location
    return "No Restaurant found"
    
if __name__ == '__main__':
  findARestaurant("Pizza", "Tokyo, Japan")
  findARestaurant("Tacos", "Jakarta, Indonesia")
  findARestaurant("Tapas", "Maputo, Mozambique")
  findARestaurant("Falafel", "Cairo, Egypt")
  findARestaurant("Spaghetti", "New Delhi, India")
  findARestaurant("Cappuccino", "Geneva, Switzerland")
  findARestaurant("Sushi", "Los Angeles, California")
  findARestaurant("Steak", "La Paz, Bolivia")
  findARestaurant("Gyros", "Sydney Australia") 