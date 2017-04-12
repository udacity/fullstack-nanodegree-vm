from flask import Flask
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Restaurant, MenuItem

engine = create_engine('sqlite:///restaurantmenu.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

app = Flask(__name__)


@app.route('/')
@app.route('/hello')
def HelloWorld():
    restaurants = session.query(Restaurant).all()
    output = ''
    for r in restaurants:
        output += '<a href="restaurants/%s" > %s </a>'%(r.id,r.name)
        output += '<br>'
    return output


@app.route('/restaurants/<int:restaurant_id>/')
def restaurantMenu(restaurant_id):
    restaurant = session.query(Restaurant).filter_by(id=restaurant_id).one()
    items = session.query(MenuItem).filter_by(restaurant_id=restaurant_id)
    output = ''
    output += restaurant.name
    output += '<br>'
    for item in items:
        output += '---- %s for %s' % (item.name, item.price)
        output += '<br>'
    return output

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=4000)
