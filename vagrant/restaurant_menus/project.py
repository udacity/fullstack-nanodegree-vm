from flask import Flask, render_template, request
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

restuarants_url = '/restuarants/<int:restaurant_id>/'

@app.route('/')
@app.route(restuarants_url)
def restaruant_menu(restaurant_id):
    restaurant = (
        session.query(Restaurant).filter_by(id = restaurant_id).first())
    items = session.query(MenuItem).filter_by(restaurant_id = restaurant.id)
    return render_template('menu.html', restaurant=restaurant, items=items)

@app.route(restuarants_url + 'new', method=['GET', 'POST'])
@app.route(restuarants_url + 'new/', method=['GET', 'POST'])
def new_menu_item(restaurant_id):
    return "page to create a new menu item. Task 1 complete!"

@app.route(restuarants_url + '<int:menu_id>/edit')
@app.route(restuarants_url + '<int:menu_id>/edit/')
def editMenuItem(restaurant_id, menu_id):
    return "page to edit a menu item. Task 2 complete!"

@app.route(restuarants_url + '<int:menu_id>/delete')
@app.route(restuarants_url + '<int:menu_id>/delete/')
def deleteMenuItem(restaurant_id, menu_id):
    return "page to delete a menu item. Task 3 complete!"

if __name__ == '__main__':
    app.debug = True
    app.run(host = '0.0.0.0', port = 5000)