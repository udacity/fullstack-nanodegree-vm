from flask import Flask, render_template, url_for, request, redirect, flash
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Restaurant, MenuItem
app = Flask(__name__)
from database_connect import *
from html_strings import *

session = dbConnect()

@app.route('/')
@app.route('/restaurant')
def restaurantList():
    return "Hello Word!"

@app.route('/restaurant/<int:restaurant_id>/')
def restaurantMenu(restaurant_id):
    restaurant = session.query(Restaurant).filter_by(id=restaurant_id).one()
    if restaurant is None:
        flash("could not find the restaurant!")
        return redirect(url_for('restaurant'))
    items = session.query(MenuItem).filter_by(restaurant_id=restaurant.id)
    ans = render_template('menu.html', restaurant=restaurant, items=items)
    return ans
    """output = ''
    output += "<h1> Restaurant:" + restaurant.name +"</h1>"
    for i in items:
        output += i.name + "<br>"+ i.description +"     ........." +str(i.price) +"<br>"
        output += '<br>'
    return output"""


@app.route('/restaurant/<int:restaurant_id>/new', methods=['GET', 'POST'])
def newMenuItem(restaurant_id):
    restaurant = session.query(Restaurant).filter_by(id=restaurant_id).one()
    if restaurant is None:
        flash("could not find the restaurant!")
        return redirect(url_for('restaurant'))
    if request.method == 'POST':
        newItem = MenuItem(name=request.form['new_menu_item'], description=request.form[
                           'new_menu_description'], price=request.form['new_menu_price'], restaurant_id=restaurant_id)
        session.add(newItem)
        session.commit()
        flash("Succesfully created the new menu item!")
        return redirect(url_for('restaurantMenu', restaurant_id=restaurant_id))
    else:
        return render_template('newmenuitem.html', restaurant=restaurant)
    #"page to create a new menu item. Task 1 complete!"

# Task 2: Create route for editMenuItem function here

@app.route('/restaurant/<int:restaurant_id>/Menu/<int:menu_id>/edit', methods=['GET', 'POST'])
def editMenuItem(restaurant_id, menu_id):
    restaurant = session.query(Restaurant).filter_by(id=restaurant_id).one()
    if restaurant is None:
        flash("could not find the restaurant!")
        return redirect(url_for('restaurant'))

    item = session.query(MenuItem).filter_by(id=menu_id, restaurant_id=restaurant_id).one()
    if item is None:
        flash("could not find the menu item!")
        return redirect(url_for('restaurant'))

    if request.method == 'POST':
        item.name = request.form['edit-menu-name']
        item.description=request.form['edit-menu-description']
        item.price=request.form['edit-menu-price']
        session.add(item)
        session.commit()
        flash("Succesfully edited the menu item!")
        return redirect(url_for('restaurantMenu', restaurant_id=restaurant_id))
    else:
        return render_template('editmenuitem.html', restaurant=restaurant, item = item)
    return "page to edit a menu item. Task 2 complete!"

# Task 3: Create a route for deleteMenuItem function here

@app.route('/restaurant/<int:restaurant_id>/Menu/<int:menu_id>/delete', methods=['GET', 'POST'])
def deleteMenuItem(restaurant_id, menu_id):
    restaurant = session.query(Restaurant).filter_by(id=restaurant_id).one()
    if restaurant is None:
        flash("could not find the restaurant!")
        return redirect(url_for('restaurant'))

    item = session.query(MenuItem).filter_by(id=menu_id, restaurant_id=restaurant_id).one()
    if item is None:
        flash("could not find the restaurant!")
        return redirect(url_for('restaurant'))

    if request.method == 'POST':
        session.delete(item)
        session.commit()
        flash("Succesfully deleted the menu item!")
        return redirect(url_for('restaurantMenu', restaurant_id=restaurant_id))
    else:
        return render_template('deletemenuitem.html', restaurant=restaurant, item = item)
    return "page to delete a menu item. Task 3 complete!"

if __name__ == '__main__':
    app.secret_key = 'super_secret_key'
    app.debug = True
    app.run(host='0.0.0.0', port=5000)
