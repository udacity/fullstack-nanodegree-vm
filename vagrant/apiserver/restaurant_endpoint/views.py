from findARestaurant import findARestaurant
from restaurant_models import Base, Restaurant
from flask import Flask, jsonify, request
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine

import sys
import codecs
sys.stdout = codecs.getwriter('utf8')(sys.stdout)
sys.stderr = codecs.getwriter('utf8')(sys.stderr)




#foursquare_client_id = ''

#foursquare_client_secret = ''

#google_api_key = ''

engine = create_engine('sqlite:///restaruants.db')

Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()
app = Flask(__name__)

@app.route('/restaurants', methods = ['GET', 'POST'])
def all_restaurants_handler():
  #YOUR CODE HERE
  if request.method == 'GET':
    #Call the method to Get all of the restaurants
    return getAllRestaurants()
  elif request.method == 'POST':
    #Call the method to make a new restaurant
    print "Making a New restaurant"    
    location = request.args.get('location', '')
    mealType = request.args.get('mealType', '')
    print location
    print mealType
    restaurant = findARestaurant(mealType,location)
    if restaurant:
    	return makeANewRestaurant(restaurant)
    else:
    	return "No restaurant"	
    
@app.route('/restaurants/<int:id>', methods = ['GET','PUT', 'DELETE'])
def restaurant_handler(id):
  #YOUR CODE HERE
  if request.method == 'GET':
    return getRestaurant(id)
    
#Call the method to edit a specific restaurant  
  elif request.method == 'PUT':
    name = request.args.get('name', '')
    address = request.args.get('address', '')
    image = request.args.get('image','')
    return updateRestaurant(id,name, address,image)
    
 #Call the method to remove a restaurant 
  elif request.method == 'DELETE':
    return deleteRestaurant(id)

def getAllRestaurants():
  restaurants = session.query(Restaurant).all()
  return jsonify(restaurants=[i.serialize for i in restaurants])

def getRestaurant(id):
  restaurant = session.query(Restaurant).filter_by(id = id).one()
  return jsonify(restaurant=restaurant.serialize) 
  
def makeANewRestaurant(restaurantInfo):
  restaurant = Restaurant(restaurant_name = restaurantInfo['name'], restaurant_address = restaurantInfo['address'],restaurant_image=restaurantInfo['image_url'])
  session.add(restaurant)
  session.commit()
  return jsonify(restaurant=restaurant.serialize)

def updateRestaurant(id,name, address,image):
  restaurant = session.query(Restaurant).filter_by(id = id).one()
  if not name:
    restaurant.restaurant_name = name
  if not address:
    restaurant.restaurant_address = address
  if not image:
    restaurant.restaurant_image = image    
  session.add(restaurant)
  session.commit()
  return jsonify(restaurant=restaurant.serialize) 

def deleteRestaurant(id):
  restaurant = session.query(Restaurant).filter_by(id = id).one()
  session.delete(restaurant)
  session.commit()
  return "Removed Restaurant with id %s" % id

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5000)

