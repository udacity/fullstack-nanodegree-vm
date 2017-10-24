from flask import Flask, render_template, request, redirect, url_for, flash, jsonify

app = Flask(__name__)

# import CRUD Operations
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_initial import Base, Restaurant, MenuItem

# Create session and connect to DB
engine = create_engine('sqlite:///restaurantmenu.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()


@app.route('/')
@app.route('/home/')
def welcome_home():
    return render_template('welcome_home.html')


@app.route('/restaurants/')
def show_restaurant():
    Restaurants = session.query(Restaurant).all()
    return render_template('show_restaurant.html', restaurants=Restaurants)


@app.route('/restaurants/new/', methods=["GET", "POST"])
def new_restaurant():
    if request.method == 'POST':
        newRestaurant = Restaurant(name=request.form['name'])
        session.add(newRestaurant)
        session.commit()
        flash(request.form['name'] + ' Created!')
        return redirect(url_for('show_restaurant', restaurants=Restaurant))
    else:
        return render_template('new_restaurant.html')


@app.route('/restaurants/<int:restaurant_id>/edit/', methods=["GET", "POST"])
def edit_restaurant(restaurant_id):
    editrestaurant = session.query(Restaurant).filter_by(id=restaurant_id).one()
    if request.method == "POST":
        if request.form['name']:
            editrestaurant.name = request.form['name']
        session.add(editrestaurant)
        session.commit()
        flash(request.form['name'] + ' Edited!')
        return redirect(url_for('show_restaurant'))
    else:
        return render_template('edit_restaurant.html', id=restaurant_id, item=editrestaurant)


@app.route('/restaurants/<int:restaurant_id>/delete', methods=["GET", "POST"])
def delete_restaurant(restaurant_id):
    itemToDelete = session.query(Restaurant).filter_by(id=restaurant_id).one()
    if request.method == "POST":
        session.delete(itemToDelete)
        session.commit()
        flash(itemToDelete.name + ' Deleted!')
        return redirect(url_for('show_restaurant'))
    else:
        return render_template('delete_menu.html', id=restaurant_id, item=itemToDelete)


@app.route('/restaurants/<int:restaurant_id>/menu')
def show_menu(restaurant_id):
    restaurant = session.query(Restaurant).filter_by(id=restaurant_id).one()
    items = session.query(MenuItem).filter_by(restaurant_id=restaurant.id).all()
    if items:
        return render_template('show_menu.html', restaurant=restaurant, items=items)
    else:
        return render_template('no_menu.html', restaurant=restaurant)


@app.route('/restaurants/<int:restaurant_id>/menu/new', methods=["GET", "POST"])
def new_menu(restaurant_id):
    if request.method == 'POST':
        newItem = MenuItem(name=request.form['name'],
                           description=request.form['description'],
                           price=request.form['price'],
                           course=request.form['course'],
                           restaurant_id=restaurant_id)
        session.add(newItem)
        session.commit()
        flash(request.form['name'] + ' Menu Item Created!')
        return redirect(url_for('show_menu', restaurant_id=restaurant_id))
    else:
        return render_template('new_menu.html', restaurant_id=restaurant_id)


@app.route('/restaurants/<int:restaurant_id>/<int:menu_id>/edit/', methods=["GET", "POST"])
def edit_menu(restaurant_id, menu_id):
    editItem = session.query(MenuItem).filter_by(id=menu_id).one()
    if request.method == "POST":
        if request.form['name']:
            editItem.name = request.form['name']
        session.add(editItem)
        session.commit()
        flash(request.form['name'] + ' Menu Item Edited!')
        return redirect(url_for('show_menu', restaurant_id=restaurant_id))
    else:
        return render_template('edit_menu.html', restaurant_id=restaurant_id, menu_id=menu_id, item=editItem)


@app.route('/restaurants/<int:restaurant_id>/<int:menu_id>/delete/', methods=["GET", "POST"])
def delete_menu(restaurant_id, menu_id):
    itemToDelete = session.query(MenuItem).filter_by(id=menu_id).one()
    if request.method == "POST":
        session.delete(itemToDelete)
        session.commit()
        flash(itemToDelete.name + ' Menu Item Deleted!')
        return redirect(url_for('show_menu', restaurant_id=restaurant_id))
    else:
        return render_template('delete_menu.html', restaurant_id=restaurant_id, menu_id=menu_id, item=itemToDelete)


# route for JSON API
@app.route('/restaurants/<int:restaurant_id>/menu/JSON')
def restaurantMenuJSON(restaurant_id):
    restaurant = session.query(Restaurant).filter_by(id=restaurant_id).one()
    items = session.query(MenuItem).filter_by(restaurant_id=restaurant.id).all()
    return jsonify(MenuItems=[item.serialize for item in items])


@app.route('/restaurants/<int:restaurant_id>/<int:menu_id>/JSON')
def MenuItemJSON(restaurant_id, menu_id):
    item = session.query(MenuItem).filter_by(id=menu_id).one()
    return jsonify(MenuItems=[item.serialize])


if __name__ == '__main__':
    app.secret_key = 'super_secret_key1'
    app.debug = True
    app.run(host='0.0.0.0', port=9000)
