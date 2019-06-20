from flask import Flask, render_template, request, redirect, url_for
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from database_setup import Base, Restaurant, MenuItem

app = Flask(__name__)


def create_sql_session():
    engine = create_engine('sqlite:///restaurantmenu.db')
    Base.metadata.create_all(engine)
    DBSession = sessionmaker(bind = engine)
    session = DBSession()
    return session

@app.route('/')
@app.route('/restaurants/<int:restaurant_id>')
def restaurantMenu(restaurant_id):
    session = create_sql_session()
    restaurant = session.query(Restaurant).get(restaurant_id)
    items = session.query(MenuItem).filter_by(restaurant_id=restaurant_id)
    return render_template(
        'menu.html', 
        restaurant=restaurant,
        items=items
    )

@app.route('/restaurant/<int:restaurant_id>/new/', methods=['GET', 'POST'])
def newMenuItem(restaurant_id):
    if request.method == 'POST':
        session = create_sql_session()
        newItem = MenuItem(
            name=request.form['name'], restaurant_id=restaurant_id)
        session.add(newItem)
        session.commit()
        return redirect(url_for('restaurantMenu', restaurant_id=restaurant_id))
    else:
        return render_template('newmenuitem.html', restaurant_id=restaurant_id)


@app.route('/restaurants/<int:restaurant_id>/<int:menu_id>/edit',
    methods = ['GET', 'POST'])
def editMenuItem(restaurant_id, menu_id):
    session = create_sql_session()
    edited_item = session.query(MenuItem).filter_by(id = menu_id).one()
    if request.method == 'POST':
        if request.form['name']:
            edited_item.name = request.form['name']
        if request.form['description']:
            edited_item.description = request.form['description']
        if request.form['price']:
            edited_item.price = request.form['price']
        if request.form['course']:
            edited_item.course = request.form['course']
        session.add(edited_item)
        session.commit()
        return redirect(
            url_for('restaurantMenu',restaurant_id=restaurant_id))
    else:
        return render_template(
            'editmenuitem.html',
            restaurant_id=restaurant_id,
            menu_id = menu_id,
            item = edited_item
        )



@app.route('/restaurants/<int:restaurant_id>/<int:menu_id>/delete',
    methods = ['GET', 'POST'])
def deleteMenuItem(restaurant_id, menu_id):
    session = create_sql_session()
    deleted_item = session.query(MenuItem).get(menu_id)
    if request.method == 'POST':
        session.delete(deleted_item)
        session.commit()
        return redirect(url_for('restaurantMenu', restaurant_id=restaurant_id))
    else:
        return render_template(
            'deletemenuitem.html',
            restaurant_id=restaurant_id,
            menu_id = menu_id,
            item = deleted_item
        )


if __name__ == '__main__':
    app.debug = True
    app.run(host = '0.0.0.0', port = 5000)