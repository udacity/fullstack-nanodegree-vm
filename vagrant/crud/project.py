from flask import Flask
app = Flask(__name__)
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from database_setup import Base, Restaurant, MenuItem

def create_sql_session():
    engine = create_engine('sqlite:///restaurantmenu.db')
    Base.metadata.create_all(engine)
    DBSession = sessionmaker(bind = engine)
    session = DBSession()
    return session

@app.route('/')
@app.route('/restaurants/<int:restaurant_id>')
def HelloWorld(restaurant_id):
    session = create_sql_session()
    restaurant = session.query(Restaurant).get(restaurant_id)
    items = session.query(MenuItem).filter_by(restaurant_id=restaurant_id)
    output = '<html><body>'
    output += '<h1>'+restaurant.name+'</h1>'
    output += '<h2>Menu</h2>'
    output += '<ul>'
    for i in items:
        output += '<li><h3>'+i.name+'</h3></li>'
        output += '<li><h3>'+i.price+'</h3></li>'
        output += '<li><h3>'+i.description+'</h3></li>'
        output += '<br>'
    output += '</ul></body></html>'
    return output

if __name__ == '__main__':
    app.debug = True
    app.run(host = '0.0.0.0', port = 5000)