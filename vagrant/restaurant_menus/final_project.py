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

# Common urls
restaurant_url = '/restaurant/<int:restaurant_id>'
menu_id_url = restaurant_url + '/menu/<int:menu_id>'

#Methods used
methods = ['GET', 'POST']

def get_restaurant_by_id(restaurant_id):
    """
    Function for getting a restaurant object given the restaurant id.
    """
    return session.query(Restaurant).filter_by(id = restaurant_id).first()

def get_menu_item_by_id(menu_id):
    """
    Function for getting a menu item object given the menu item id.
    """
    return session.query(MenuItem).filter_by(id = menu_id).first()

def get_restaurant_menu_items_by_id(restaurant_id):
    """Returns the menu items for the given restaurant id."""
    return session.query(MenuItem).filter_by(
        restaurant_id = restaurant_id).all()

@app.route('/')
@app.route('/restaurants/')
def all_restaurants():
    restaurants = session.query(Restaurant).all()
    return render_template('all_restaurants.html', restaurants=restaurants)

@app.route('/restaurants/json/')
@app.route('/restaurants/JSON/')
def all_restaurants_json():
    restaurants = session.query(Restaurant).all()
    return jsonify(Restaurant=[rest.serialize for rest in restaurants])


@app.route('/restaurant/new/', methods=methods)
def new_restaurant():
    if request.method == 'POST':
        restaurant_name = request.form['name']
        if restaurant_name:
            new_rest = Restaurant(name=request.form['name'])
            session.add(new_rest)
            session.commit()
            flash("New restaurant, %s, created!" % new_rest.name)
            return redirect(url_for('all_restaurants'))
        else:
            flash("Please enter a restaurant name!")
            return render_template('new_restaurant.html')

    else:
        return render_template('new_restaurant.html')

@app.route(restaurant_url + '/')
@app.route(restaurant_url + '/menu/')
def restaurant_menu(restaurant_id):
    restaurant = get_restaurant_by_id(restaurant_id)
    items = get_restaurant_menu_items_by_id(restaurant.id)
    return render_template('menu.html', restaurant=restaurant, items=items)

@app.route(restaurant_url + '/menu/json/')
@app.route(restaurant_url + '/menu/JSON/')
def restaurant_menu_json(restaurant_id):
    restaurant = get_restaurant_by_id(restaurant_id)
    items = get_restaurant_menu_items_by_id(restaurant_id)
    return jsonify(MenuItem=[item.serialize for item in items])

@app.route(restaurant_url + '/edit/', methods=methods)
def edit_restaurant(restaurant_id):
    restaurant = get_restaurant_by_id(restaurant_id)
    if request.method == 'POST':
        restaurant_name = request.form['name']
        if restaurant_name:
            old_name = restaurant.name
            restaurant.name = restaurant_name
            session.add(restaurant)
            session.commit()
            flash('%s is now named %s!' % (old_name, restaurant.name))
            return redirect(url_for('restaurant_menu',
                                    restaurant_id=restaurant.id))
        else:
            flash("Please enter a restaurant name!")
            return render_template('edit_restaurant.html',
                                   restaurant=restaurant,
                                   restaurant_id=restaurant_id)
    if restaurant:
        return render_template('edit_restaurant.html',
                               restaurant=restaurant,
                               restaurant_id=restaurant_id)
    else:
        return redirect(url_for('all_restaurants'))

@app.route(restaurant_url + '/delete/', methods=methods)
def delete_restaurant(restaurant_id):
    restaurant = get_restaurant_by_id(restaurant_id)
    if restaurant:
        if request.method == 'POST':
            if request.form['Delete']:
                deleted_name = restaurant.name
                session.delete(restaurant)
                session.commit()
                flash('%s was deleted.' % deleted_name)
                return redirect(url_for('all_restaurants'))
        else:
            return render_template('delete_restaurant.html',
                                   restaurant=restaurant,
                                   restaurant_id=restaurant_id)
    else:
        return redirect(url_for('all_restaurants'))

@app.route(restaurant_url + '/menu/new/', methods=methods)
def new_menu_item(restaurant_id):
    restaurant = get_restaurant_by_id(restaurant_id)
    if restaurant:
        if request.method == 'POST':
            new_item_data = {
                'name' : request.form['name'],
                'price' : request.form['price'],
                'description' : request.form['description'],
                'course' : request.form['course']               
            }
            missing_items = []
            for name, data in new_item_data.iteritems():
                if not new_item_data[name]:
                    missing_items.append(name)
            if missing_items:
                flash("Please enter an item %s!" % missing_items)
                return render_template('new_menu_item.html',
                                       restaurant=restaurant,
                                       name_val=new_item_data['name'],
                                       desc_val=new_item_data['description'],
                                       price_val=new_item_data['price'],
                                       course_val=new_item_data['course'])
            else:
                new_item = MenuItem(name=new_item_data['name'],
                                    description=new_item_data['description'],
                                    price=int(new_item_data['price']),
                                    course=new_item_data['course'],
                                    restaurant_id=restaurant.id)
                session.add(new_item)
                session.commit()
                flash("New menu item, %s, created!" % new_item.name)
                return redirect(url_for(
                    'restaurant_menu', restaurant_id=restaurant.id))
        else:
            return render_template('new_menu_item.html',
                                   restaurant=restaurant)
    else:
        return redirect(url_for('all_restaurants'))

@app.route(menu_id_url + '/edit/', methods=methods)
def edit_menu_item(restaurant_id, menu_id):
    restaurant = get_restaurant_by_id(restaurant_id)
    edited_item = get_menu_item_by_id(menu_id)
    if not restaurant or not edited_item:
        return redirect(url_for('all_restaurants'))
    else:
        if edited_item.restaurant_id != restaurant.id:
            flash('Sorry, that menu item does not belong to this restaurant.')
            return redirect('restaurant_menu', restaurant_id=restaurant.id)
        else:
            if request.method == 'POST':
                new_item_data = {
                    'name' : request.form['name'],
                    'price' : request.form['price'],
                    'description' : request.form['description'],
                    'course' : request.form['course']
                }
                missing_items = []
                for name, data in new_item_data.iteritems():
                    if not new_item_data[name]:
                        missing_items.append(name)
                if missing_items:
                    flash("Please enter an item %s!" % missing_items)
                    return render_template('edit_menu_item.html',
                                           restaurant=restaurant,
                                           item=edited_item)
                else:
                    edited_item.name = new_item_data['name']
                    edited_item.price = new_item_data['price']
                    edited_item.description = new_item_data['description']
                    edited_item.course = new_item_data['course']
                    session.add(edited_item)
                    session.commit()
                    flash('%s has been updated!' % (edited_item.name))
                    return redirect(url_for(
                        'restaurant_menu', restaurant_id=restaurant.id))
            else:
                return render_template('edit_menu_item.html',
                                       restaurant=restaurant,
                                       item=edited_item)

@app.route(menu_id_url + '/delete/', methods=methods)
def delete_menu_item(restaurant_id, menu_id):
    restaurant = get_restaurant_by_id(restaurant_id)
    to_delete_item = get_menu_item_by_id(menu_id)
    if not restaurant or not to_delete_item:
        return redirect(url_for('all_restaurants'))
    else:
        if to_delete_item.restaurant_id != restaurant.id:
            flash('Sorry, that menu item does not belong to this restaurant.')
            return redirect('restaurant_menu', restaurant_id=restaurant.id)
        else:
            if request.method == 'POST':
                if request.form['Delete']:
                    session.delete(to_delete_item)
                    session.commit()
                    flash('%s was deleted.' % to_delete_item.name)
                return redirect(url_for('restaurant_menu',
                                        restaurant_id=restaurant_id))
            else:
                return render_template('delete_menu_item.html',
                                       restaurant=restaurant,
                                       item=to_delete_item)

@app.route(menu_id_url + '/json/')
@app.route(menu_id_url + '/JSON/')
def menu_item_json(restaurant_id, menu_id):
    menu_item = get_menu_item_by_id(menu_id)
    return jsonify(MenuItems=[menu_item.serialize])



if __name__ == '__main__':
    app.secret_key = 'super_secret_key'
    app.debug = True
    app.run(host = '0.0.0.0', port = 5000)