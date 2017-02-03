from flask import Flask, render_template, url_for, redirect, request, flash, jsonify
app = Flask(__name__)

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Restaurant, MenuItem

restuarant_url = '/restaurant/<int:restaurant_id>'
menu_id_url = restuarant_url + '/menu/<int:menu_id>'

def render_message(message):
    return render_template('message.html', message=message)

@app.route('/')
@app.route('/restaurants')
@app.route('/restaurants/')
def all_restaurants():
    return render_message("This page will show all my restaurants.")

@app.route('/restaurant/new')
@app.route('/restaurant/new/')
def new_restaurant():
    return render_message("This page will be for making a new restaurant.")

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