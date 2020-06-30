from database_setup import Base, Restaurant, MenuItem
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from flask import Flask, render_template, url_for, request, redirect, flash, jsonify
app = Flask(__name__)

engine = create_engine("sqlite:///restaurantmenu.db")
Base.metadata.bind = engine


@app.route("/")
@app.route("/restaurant/")
def showRestaurants():
    if request.path == "/":
        return redirect(url_for("showRestaurants"))

    DBSession = sessionmaker(bind=engine)
    session = DBSession()
    restaurants = session.query(Restaurant).all()

    return render_template("restaurantlist.html", restaurants=restaurants)


@app.route("/restaurant/new/", methods=["GET", "POST"])
def createRestaurant():
    DBSession = sessionmaker(bind=engine)
    session = DBSession()
    if request.method == "POST":
        newRestaurant = Restaurant(name=request.form["name"])
        session.add(newRestaurant)
        session.commit()
        flash("New Restaurant created: %s" % newRestaurant.name)
        return redirect(url_for("showRestaurants"))
    else:
        # return "this page will create new restaurants"
        return render_template("newrestaurant.html")


@app.route("/restaurant/<int:restaurant_id>/edit/", methods=["GET", "POST"])
def editRestaurant(restaurant_id):
    DBSession = sessionmaker(bind=engine)
    session = DBSession()
    if request.method == "POST":
        restaurantToEdit = session.query(
            Restaurant).filter_by(id=restaurant_id).one()
        restaurantToEdit.name = request.form["name"]
        session.commit()
        flash("Edited Restaurant name: %s" % restaurantToEdit.name)
        return redirect(url_for("showRestaurants"))
    else:
        restaurant = session.query(
            Restaurant).filter_by(id=restaurant_id).one()
        # return "this page will edit restaurant with id: %s" % restaurant_id
        return render_template("editrestaurant.html", restaurant=restaurant)


@app.route("/restaurant/<int:restaurant_id>/delete/", methods=["GET", "POST"])
def deleteRestaurant(restaurant_id):
    DBSession = sessionmaker(bind=engine)
    session = DBSession()
    if request.method == "POST":
        restaurantToDelete = session.query(
            Restaurant).filter_by(id=restaurant_id).one()
        session.delete(restaurantToDelete)
        session.commit()
        flash("Deleted Restaurant: %s" % restaurantToDelete.name)
        return redirect(url_for("showRestaurants"))
    else:
        restaurant = session.query(
            Restaurant).filter_by(id=restaurant_id).one()
        # return "this page will delete restaurant with id: %s" % restaurant_id
        return render_template("deleterestaurant.html", restaurant=restaurant)


@app.route("/restaurant/<int:restaurant_id>/")
@app.route("/restaurant/<int:restaurant_id>/menu/")
def showMenu(restaurant_id):
    if request.path == "/restaurant/%s/" % restaurant_id:
        return redirect(url_for("showMenu", restaurant_id=restaurant_id))
    # return "this page will show the menu for restaurant %s" % restaurant_id
    DBSession = sessionmaker(bind=engine)
    session = DBSession()
    restaurant = session.query(Restaurant).filter_by(id=restaurant_id).one()
    items = session.query(MenuItem).filter_by(restaurant_id=restaurant.id)
    return render_template("menu.html", restaurant=restaurant, items=items)


@app.route("/restaurant/<int:restaurant_id>/menu/new/", methods=["GET", "POST"])
def createMenuItem(restaurant_id):
    DBSession = sessionmaker(bind=engine)
    session = DBSession()
    if request.method == "POST":
        newItem = MenuItem(name=request.form["name"], price=request.form["price"],
                           description=request.form["description"], restaurant_id=restaurant_id)
        session.add(newItem)
        session.commit()
        flash("new menu item created: %s" % newItem.name)
        return redirect(url_for("showMenu", restaurant_id=restaurant_id))
    else:
        # return "this page will create a new menu item for restaurant %s" % restaurant_id
        restaurant = session.query(
            Restaurant).filter_by(id=restaurant_id).one()
        return render_template("newmenuitem.html", restaurant=restaurant)


@app.route("/restaurant/<int:restaurant_id>/menu/<int:menu_id>/edit/", methods=["GET", "POST"])
def editMenuItem(restaurant_id, menu_id):
    DBSession = sessionmaker(bind=engine)
    session = DBSession()
    if request.method == "POST":
        item = session.query(MenuItem).filter_by(
            restaurant_id=restaurant_id, id=menu_id).one()
        item.name = request.form["name"]
        item.description = request.form["description"]
        item.price = request.form["price"]
        session.commit()
        flash("edited menu item: %s" % item.name)
        return redirect(url_for("showMenu", restaurant_id=restaurant_id))
    else:
        # return "this page will edit menu item with id: %s" % menu_id
        item = session.query(MenuItem).filter_by(
            restaurant_id=restaurant_id, id=menu_id).one()
        return render_template("editmenuitem.html", item=item)


@app.route("/restaurant/<int:restaurant_id>/menu/<int:menu_id>/delete/", methods=["GET", "POST"])
def deleteMenuItem(restaurant_id, menu_id):
    DBSession = sessionmaker(bind=engine)
    session = DBSession()
    if request.method == "POST":
        item = session.query(MenuItem).filter_by(
            restaurant_id=restaurant_id, id=menu_id).one()
        session.delete(item)
        session.commit()
        flash("deleted menu item: %s" % item.name)
        return redirect(url_for("showMenu", restaurant_id=restaurant_id))
    else:
        # return "this page will delete menu item with id: %s" % menu_id
        item = session.query(MenuItem).filter_by(
            restaurant_id=restaurant_id, id=menu_id).one()
        return render_template("deletemenuitem.html", item=item)


@app.route("/restaurant/JSON/")
def restaurantJSON():
    DBSession = sessionmaker(bind=engine)
    session = DBSession()
    restaurants = session.query(Restaurant).all()
    return jsonify(Restaurants=[r.serialize for r in restaurants])


@app.route("/restaurant/<int:restaurant_id>/JSON/")
@app.route("/restaurant/<int:restaurant_id>/menu/JSON/")
def menuItemJSON(restaurant_id):
    if request.path == "/restaurant/%s/JSON/" % restaurant_id:
        return redirect(url_for("menuItemJSON", restaurant_id=restaurant_id))
    DBSession = sessionmaker(bind=engine)
    session = DBSession()
    restaurant = session.query(Restaurant).filter_by(id=restaurant_id).one()
    menu = session.query(MenuItem).filter_by(restaurant_id=restaurant.id).all()
    return jsonify(MenuItems=[item.serialize for item in menu])


@app.route("/restaurant/<int:restaurant_id>/menu/<int:menu_id>/JSON/")
def menuJSON(restaurant_id, menu_id):
    DBSession = sessionmaker(bind=engine)
    session = DBSession()
    restaurant = session.query(Restaurant).filter_by(id=restaurant_id).one()
    menuItem = session.query(MenuItem).filter_by(restaurant_id=restaurant.id, id=menu_id).one()
    return jsonify(Item=[menuItem.serialize])


if __name__ == "__main__":
    app.secret_key = "something-very-secret"
    app.debug = True
    app.run(host="0.0.0.0", port=5000)
