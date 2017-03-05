from flask import Flask, render_template
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Restaurant, MenuItem, engine


app = Flask(__name__)

engine = create_engine('sqlite:///restaurantmenu.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()


@app.route('/')
@app.route('/restaurants/<int:restaurant_id>/')
def restaurant_menu(restaurant_id):
    restaurant = session.query(Restaurant).filter_by(id=restaurant_id).one()
    items = session.query(MenuItem).filter_by(restaurant_id=restaurant_id)

    return render_template('restaurant/menu.html', restaurant=restaurant, items=items)


@app.route('/restaurants/<int:restaurant_id>/new-menu-item/')
def new_menu_item(restaurant_id):
    return "Create a new menu item"


@app.route('/restaurants/<int:restaurant_id>/<int:item_id>/edit/')
def edit_menu_item(restaurant_id, item_id):
    return "Edit the menu item"


@app.route('/restaurants/<int:restaurant_id>/<int:item_id>/delete/')
def delete_menu_item(restaurant_id, item_id):
    return "Delete the menu item"


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5000)
