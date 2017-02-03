from flask import Flask, render_template, url_for, redirect, request, flash, jsonify
app = Flask(__name__)

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Restaurant, MenuItem

#Fake Restaurants
restaurant = {'name': 'The CRUDdy Crab', 'id': '1'}

restaurants = [{'name': 'The CRUDdy Crab', 'id': '1'}, {'name':'Blue Burgers', 'id':'2'},{'name':'Taco Hut', 'id':'3'}]


#Fake Menu Items
items = [ {'name':'Cheese Pizza', 'description':'made with fresh cheese', 'price':'$5.99','course' :'Entree', 'id':'1'}, {'name':'Chocolate Cake','description':'made with Dutch Chocolate', 'price':'$3.99', 'course':'Dessert','id':'2'},{'name':'Caesar Salad', 'description':'with fresh organic vegetables','price':'$5.99', 'course':'Entree','id':'3'},{'name':'Iced Tea', 'description':'with lemon','price':'$.99', 'course':'Beverage','id':'4'},{'name':'Spinach Dip', 'description':'creamy dip with fresh spinach','price':'$1.99', 'course':'Appetizer','id':'5'} ]
item =  {'name':'Cheese Pizza','description':'made with fresh cheese','price':'$5.99','course' :'Entree'}

restuarant_url = '/restaurant/<int:restaurant_id>'
menu_id_url = restuarant_url + '/menu/<int:menu_id>'

def render_message(message):
    return render_template('message.html', message=message)

@app.route('/')
@app.route('/restaurants')
@app.route('/restaurants/')
def all_restaurants():
    #restaurants = session.query(Restaurant).all()
    if len(restaurants) <= 0:
        return render_template('all_restaurants.html', no_restaurants = 0)
    else:
        return render_template('all_restaurants.html', restaurants=restaurants)

@app.route('/restaurant/new')
@app.route('/restaurant/new/')
def new_restaurant():
    return render_template('new_restaurant.html')

@app.route(restuarant_url)
@app.route(restuarant_url + '/')
@app.route(restuarant_url + '/menu')
@app.route(restuarant_url + '/menu/')
def restaurant_menu(restaurant_id):
    return render_message("This page is the menu for restaurant %s" % restaurant_id)

@app.route(restuarant_url + '/edit')
@app.route(restuarant_url + '/edit/')
def edit_restaurant(restaurant_id):
    return render_message("This page will be for editing restaurant %s" % restaurant_id)

@app.route(restuarant_url + '/delete')
@app.route(restuarant_url + '/delete/')
def delete_restaurant(restaurant_id):
    return render_message("This page will be for deleting restaurant %s" % restaurant_id)

@app.route(restuarant_url + '/menu/new')
@app.route(restuarant_url + '/menu/new/')
def new_menu_item(restaurant_id):
    return render_message("This page is for making a new menu item for restaurant %s" % restaurant_id)

@app.route(menu_id_url + '/edit')
@app.route(menu_id_url + '/edit/')
def edit_menu_item(restaurant_id, menu_id):
    return render_message("This page is for editing menu item %s" % menu_id)

@app.route(menu_id_url + '/delete')
@app.route(menu_id_url + '/delete/')
def delete_menu_item(restaurant_id, menu_id):
    return render_message("This page is for deleting menu item %s" % menu_id)



if __name__ == '__main__':
    app.secret_key = 'super_secret_key'
    app.debug = True
    app.run(host = '0.0.0.0', port = 5000)