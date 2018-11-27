#project.py
from flask import Flask, render_template, request, redirect, url_for, flash, json, jsonify

# import CRUD Operations
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Restaurant, MenuItem

app = Flask(__name__)

# Create session and connect to DB
#engine = create_engine('sqlite:///restaurantmenu.db')
engine = create_engine('sqlite:///restaurantmenu.db?check_same_thread=False')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

########################### TEST DATA START ###########################

#Fake Restaurants
#restaurant = {'name': 'The CRUDdy Crab', 'id': '1'}

#restaurants = ""
#restaurants = [{'name': 'The CRUDdy Crab', 'id': '1'}, {'name':'Blue Burgers', 'id':'2'},{'name':'Taco Hut', 'id':'3'}]

#Fake Menu Items
#items = ""
#items = [ {'name':'Cheese Pizza', 'description':'made with fresh cheese', 'price':'$5.99','course' :'Entree', 'id':'1'}, {'name':'Chocolate Cake','description':'made with Dutch Chocolate', 'price':'$3.99', 'course':'Dessert','id':'2'},{'name':'Caesar Salad', 'description':'with fresh organic vegetables','price':'$5.99', 'course':'Entree','id':'3'},{'name':'Iced Tea', 'description':'with lemon','price':'$.99', 'course':'Beverage','id':'4'},{'name':'Spinach Dip', 'description':'creamy dip with fresh spinach','price':'$1.99', 'course':'Appetizer','id':'5'} ]

#item =  {'name':'Cheese Pizza','description':'made with fresh cheese','price':'$5.99','course' :'Entree','id':'1','restaurant_id':'1'}

########################### TEST DATA END ###########################

#1. SHOW ALL RESTAURANTS
@app.route('/')
@app.route('/restaurant/', methods=['GET'])
def showRestaurants():
    restaurants = session.query(Restaurant).all()
    #return "<html><body>This page will show all my restaurants</html></body>"
    return render_template('restaurants.html', restaurants = restaurants)

#2. SHOW MENU ITEMS FOR A RESTAURANT
@app.route('/restaurant/<int:restaurant_id>/')
@app.route('/restaurant/<int:restaurant_id>/menu')
def showMenuItems(restaurant_id, methods=['GET','POST']):
    restaurant = session.query(Restaurant).filter_by(id=restaurant_id).one()
    items = session.query(MenuItem).filter_by(restaurant_id = restaurant_id)
    #return "<html><body>This page will show all menu items for restaurant %s</html></body>" % restaurant_id
    return render_template('menu.html', restaurant=restaurant, items=items)

#3. CREATE A NEW RESTAURANT
@app.route('/restaurant/new', methods=['GET','POST'])
def newRestaurant():
    if request.method == 'POST':
        createRestaurant = Restaurant(name = request.form['name'])
        session.add(createRestaurant)
        session.commit()
        flash("Created new restaurant %s" % request.form['name'])
        return redirect(url_for('showRestaurants'))
    else:
        #return "<html><body>This page will be for making a new restaurant</html></body>"
        return render_template('newRestaurant.html')

#4. EDIT AN EXISTING RESTAURANT
@app.route('/restaurant/<int:restaurant_id>/edit', methods=['GET','POST'])
def editRestaurant(restaurant_id):
    editedRestaurant = session.query(Restaurant).filter_by(id=restaurant_id).one()
    if request.method == 'POST':
        if request.form['name']:
            editedRestaurant.name = request.form['name']
        session.add(editedRestaurant)
        session.commit()
        flash("Restaurant Details Have Been Updated")
        return redirect(url_for('showRestaurants'))
    else:
        #return "<html><body>This page will be for editing restaurant %s</html></body>" % restaurant_id
        return render_template('editRestaurant.html', restaurant_id=restaurant_id, r=editedRestaurant)

#5. DELETE AN EXISTING RESTAURANT
@app.route('/restaurant/<int:restaurant_id>/delete', methods=['GET','POST'])
def deleteRestaurant(restaurant_id):
    toDeleteRestaurant = session.query(Restaurant).filter_by(id = restaurant_id).one()
    if request.method == 'POST':
        session.delete(toDeleteRestaurant)
        session.commit()
        flash("Restaurant %s has been removed" % toDeleteRestaurant.name)
        #flash("Restaurant %s has been removed" % toDeleteRestaurant.name)
        return redirect(url_for('showRestaurants'))
    else:
        #return "<html><body>This page will be for deleting restaurant %s</html></body>" % restaurant_id
        return render_template('deleteRestaurant.html', restaurant_id = restaurant_id)

#6. CREATE A NEW MENU ITEM FOR A RESTAURANT
@app.route('/restaurant/<int:restaurant_id>/menu/new', methods=['GET','POST'])
def newMenuItem(restaurant_id):
    restaurant = session.query(Restaurant).filter_by(id = restaurant_id).one()
    #items = session.query(MenuItem).filter_by(restaurant_id = restaurant_id)
    if request.method == 'POST':
        #newItem = MenuItem(name = request.form['name'], restaurant_id = restaurant_id, restaurant = restaurant)
        print("WAIT FOR IT...")
        print(request.form)
        #newItem = MenuItem(name = request.form['name'], description = request.form['description'], price = request.form['price'], course = request.form['course'], restaurant_id = restaurant_id, restaurant = restaurant)
        #session.add(newItem)
        #session.commit()
        return redirect(url_for('showMenuItems', restaurant_id=restaurant_id))
    #return "<html><body>This page will be for making a new menu item for restaurant %s</html></body>" % restaurant_id
    return render_template('newMenuItem.html', restaurant=restaurant, restaurant_id=restaurant_id)

#7. EDIT AN EXISTING MENU ITEM FOR A RESTAURANT
@app.route('/restaurant/<int:restaurant_id>/menu/<int:menu_id>/edit', methods=['GET','POST'])
def editMenuItem(restaurant_id, menu_id):
    #return "<html><body>This page will be for editing menu item %s for restaurant %s</html></body>" % (menu_id, restaurant_id)
    return render_template('editMenuItem.html', restaurant=restaurant, item=item)

#8. DELETE AN EXISTING MENU ITEM FOR A RESTAURANT
@app.route('/restaurant/<int:restaurant_id>/menu/<int:menu_id>/delete', methods=['GET','POST'])
def deleteMenuItem(restaurant_id, menu_id):
    #return "<html><body>This page will be for deleting menu item %s for restaurant %s</html></body>" % (menu_id, restaurant_id)
    return render_template('deleteMenuItem.html', restaurant=restaurant, item=item)

if __name__ == '__main__':
	app.secret_key = 'super_secret_key'
	app.debug = True
	app.run(host = '0.0.0.0', port = 5000)
