from database_setup import Base, Restaurant, MenuItem
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from flask import Flask, render_template, url_for, request, redirect, flash, jsonify
app = Flask(__name__)

engine = create_engine("sqlite:///restaurantmenu.db")
Base.metadata.bind = engine


@app.route("/restaurant/<int:restaurant_id>/menu/<int:menu_id>/JSON")
def menuItemJSONGET(restaurant_id, menu_id):
    DBSession = sessionmaker(bind=engine)
    session = DBSession()
    item = session.query(MenuItem).filter_by(
        restaurant_id=restaurant_id, id=menu_id).one()
    return jsonify(MenuItems=item.serialize)


@app.route("/restaurant/<int:restaurant_id>/menu/JSON")
def restaurantJSONGET(restaurant_id):
    DBSession = sessionmaker(bind=engine)
    session = DBSession()
    restaurant = session.query(Restaurant).filter_by(id=restaurant_id).one()
    items = session.query(MenuItem).filter_by(
        restaurant_id=restaurant_id).all()
    return jsonify(MenuItems=[i.serialize for i in items])


@app.route("/restaurant/")
def restaurantList():
    DBSession = sessionmaker(bind=engine)
    session = DBSession()
    restaurants = session.query(Restaurant).all()
    return render_template("restaurantlist.html", restaurants=restaurants)


@app.route("/restaurant/<int:restaurant_id>/")
def restaurantGET(restaurant_id):
    DBSession = sessionmaker(bind=engine)
    session = DBSession()
    restaurant = session.query(Restaurant).filter_by(id=restaurant_id).one()
    items = session.query(MenuItem).filter_by(restaurant_id=restaurant.id)
    return render_template("menu.html", restaurant=restaurant, items=items)

# Task 1: Create route for newMenuItem function here


@app.route("/restaurant/<int:restaurant_id>/new/", methods=["GET", "POST"])
def newMenuItem(restaurant_id):
    DBSession = sessionmaker(bind=engine)
    session = DBSession()
    if request.method == "POST":
        newItem = MenuItem(name=request.form["name"], price=request.form["price"],
                           description=request.form["description"], restaurant_id=restaurant_id)
        session.add(newItem)
        session.commit()
        flash("new menu item created: %s" % newItem.name)
        return redirect(url_for("restaurantGET", restaurant_id=restaurant_id))
    else:
        restaurant = session.query(
            Restaurant).filter_by(id=restaurant_id).one()
        return render_template("newmenuitem.html", restaurant=restaurant)

# Task 2: Create route for editMenuItem function here


@app.route("/restaurant/<int:restaurant_id>/<int:menu_id>/edit/", methods=["GET", "POST"])
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
        return redirect(url_for("restaurantGET", restaurant_id=restaurant_id))
    else:
        item = session.query(MenuItem).filter_by(
            restaurant_id=restaurant_id, id=menu_id).one()
        return render_template("editmenuitem.html", item=item)

# Task 3: Create a route for deleteMenuItem function here


@app.route("/restaurant/<int:restaurant_id>/<int:menu_id>/delete/", methods=["GET", "POST"])
def deleteMenuItem(restaurant_id, menu_id):
    DBSession = sessionmaker(bind=engine)
    session = DBSession()
    if request.method == "POST":
        item = session.query(MenuItem).filter_by(
            restaurant_id=restaurant_id, id=menu_id).one()
        session.delete(item)
        session.commit()
        flash("deleted menu item: %s" % item.name)
        return redirect(url_for("restaurantGET", restaurant_id=restaurant_id))
    else:
        item = session.query(MenuItem).filter_by(
            restaurant_id=restaurant_id, id=menu_id).one()
        return render_template("deletemenuitem.html", item=item)
    return "page to delete a menu item. Task 3 complete!"


if __name__ == "__main__":
    app.secret_key = "something-very-secret"
    app.debug = True
    app.run(host="0.0.0.0", port=5000)
