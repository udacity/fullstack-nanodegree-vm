from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Restaurant, MenuItem

app = Flask(__name__)

engine = create_engine('sqlite:///restaurantmenu.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

# API endpoint that sends all menus in the restaurant
@app.route('/restaurants/<int:restaurant_id>/menu/JSON')
def restaurantMenuJSON(restaurant_id):
    restaurant = session.query(Restaurant).filter_by(id=restaurant_id).one()
    items = session.query(MenuItem).filter_by(restaurant_id=restaurant_id).all()
    return jsonify(MenuItems=[i.serialize for i in items])  # serialize is defined in MenuItem of database_setup.py

# API endpoint that sends some menu in the restaurant
@app.route('/restaurants/<int:restaurant_id>/menu/<int:menu_id>/JSON')
def menuItemJSON(restaurant_id, menu_id):
    item = session.query(MenuItem).filter_by(id=menu_id).one()
    return jsonify(item.serialize)



# decorator wraps our function inside the app.route function that Flask has already created
# if either these routes get sent from the browser, tha function that we define gets executed
# <type:variable_name> is the rule to add variables to a URL
@app.route('/restaurants/<int:restaurant_id>/')
def restaurantMenu(restaurant_id):
    restaurant = session.query(Restaurant).filter_by(id=restaurant_id).one()
    items = session.query(MenuItem).filter_by(restaurant_id=restaurant_id)
    return render_template('menu.html', restaurant=restaurant, items=items)


# methods parameter takes ['GET', 'POST'] that is used for identifying a type of the request
@app.route('/restaurants/<int:restaurant_id>/new', methods=['GET', 'POST'])
def newMenuItem(restaurant_id):
    if request.method == 'POST':
        print('--------------------------------')
        print(request.form)
        newItem = MenuItem(name=request.form['name'], description=request.form['description'],
        price=request.form['price'], restaurant_id=restaurant_id)
        session.add(newItem)
        session.commit()
        flash("new menu item created!")
        return redirect(url_for('restaurantMenu', restaurant_id=restaurant_id))
    else:
        return render_template('newmenuitem.html', restaurant_id=restaurant_id)


@app.route('/restaurants/<int:restaurant_id>/<int:menu_id>/edit', methods=['GET', 'POST'])
def editMenuItem(restaurant_id, menu_id):
    targetMenu = session.query(MenuItem).filter_by(id=menu_id).one()
    if request.method == 'POST':
        if request.form['name']:
            targetMenu.name = request.form['name']
        if request.form['description']:
            targetMenu.description = request.form['description']    
        if request.form['price']:
            targetMenu.price = request.form['price']
        session.add(targetMenu)
        session.commit()
        flash("Menu Item has been edited")
        return redirect(url_for('restaurantMenu', restaurant_id=restaurant_id))
    else:
        return render_template('editmenuitem.html', restaurant_id=restaurant_id, item=targetMenu)


@app.route('/restaurants/<int:restaurant_id>/<int:menu_id>/delete', methods=['GET', 'POST'])
def deleteMenuItem(restaurant_id, menu_id):
    targetMenu = session.query(MenuItem).filter_by(restaurant_id=restaurant_id, id=menu_id).one()
    if request.method == 'POST':
        session.delete(targetMenu)
        session.commit()
        flash("Menu Item has been deleted")
        return redirect(url_for('restaurantMenu', restaurant_id=restaurant_id))
    else:
        return render_template('deletemenuitem.html', item=targetMenu)



# This if statement makes sure the server only runs if the script is executed directly from the Python interpreter,
# not used as an imported module
if __name__ == '__main__':
    app.secret_key = 'super_secret_key'
    # enable the server will reload itself each time it notices a code change
    app.debug = True
    # by default, the server is only accessible from the host machine
    # make the server publicly available like this
    app.run(host='0.0.0.0', port=5000)