"""
Legacy project data. Kept for historical records.

from flask import Flask, render_template, url_for, redirect, request, flash, jsonify
app = Flask(__name__)

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Restaurant, MenuItem


# Create database
engine = create_engine('sqlite:///restaurantmenu.db')
Base.metadata.create_all(engine)

# Create database connector
DBSession = sessionmaker(bind = engine)
session = DBSession()

restuarants_url = '/restaurants/<int:restaurant_id>/'
menu_id_url = '<int:menu_id>/'

# Making an API Endpoint (GET Request)
@app.route(restuarants_url + 'menu/JSON')
def restaurant_menu_json(restaurant_id):
    restaurant = (
        session.query(Restaurant).filter_by(id = restaurant_id).first())
    items = session.query(MenuItem).filter_by(restaurant_id = restaurant.id)
    return jsonify(MenuItems=[item.serialize for item in items])

@app.route(restuarants_url + 'menu/' + menu_id_url + 'JSON')
def menu_item_json(restaurant_id, menu_id):
    menu_item = session.query(MenuItem).filter_by(id = menu_id).one()
    return jsonify(menu_item.serialize)

@app.route('/')
@app.route('/restaurants')
@app.route('/restaurants/')
def all_restaurants():
    restaurants = session.query(Restaurant).all()
    return render_template('all_restaurants.html', restaurants=restaurants)

@app.route(restuarants_url)
def restaruant_menu(restaurant_id):
    restaurant = (
        session.query(Restaurant).filter_by(id = restaurant_id).first())
    items = session.query(MenuItem).filter_by(restaurant_id = restaurant.id)
    return render_template('menu.html', restaurant=restaurant, items=items)

@app.route(restuarants_url + 'new', methods=['GET', 'POST'])
@app.route(restuarants_url + 'new/', methods=['GET', 'POST'])
def new_menu_item(restaurant_id):
    if request.method == 'POST':
        new_item = MenuItem(name=request.form['name'],
                            restaurant_id=restaurant_id)
        session.add(new_item)
        session.commit()
        flash("New menu item, %s, created!" % new_item.name)
        return redirect(url_for('restaruant_menu', restaurant_id=restaurant_id))
    else:
        return render_template('new_menu_item.html',
                               restaurant_id=restaurant_id)

@app.route(restuarants_url + menu_id_url + 'edit', methods=['GET','POST'])
@app.route(restuarants_url + menu_id_url + 'edit/', methods=['GET','POST'])
def edit_menu_item(restaurant_id, menu_id):
    edited_item = session.query(MenuItem).filter_by(id = menu_id).one()
    if request.method == 'POST':
        if request.form['name']:
            old_name = edited_item.name
            edited_item.name = request.form['name']
            session.add(edited_item)
            session.commit()
            flash('%s is now named %s!' % (old_name, edited_item.name))
        return redirect(url_for('restaruant_menu',
                        restaurant_id=restaurant_id))
    else:
        return render_template('edit_menu_item.html',
                               restaurant_id=restaurant_id,
                               menu_id=menu_id,
                               item=edited_item)

@app.route(restuarants_url + menu_id_url + 'delete', methods=['GET', 'POST'])
@app.route(restuarants_url + menu_id_url + 'delete/', methods=['GET', 'POST'])
def delete_menu_item(restaurant_id, menu_id):
    to_delete_item = session.query(MenuItem).filter_by(id = menu_id).one()
    if request.method == 'POST':
        if request.form['Delete']:
            session.delete(to_delete_item)
            session.commit()
            flash('%s was deleted.' % to_delete_item.name)
        return redirect(url_for('restaruant_menu',
                                restaurant_id=restaurant_id))
    else:
        return render_template('delete_menu_item.html',
                               restaurant_id=restaurant_id,
                               menu_id=menu_id,
                               item=to_delete_item)

if __name__ == '__main__':
    app.secret_key = 'super_secret_key'
    app.debug = True
    app.run(host = '0.0.0.0', port = 5000)"""