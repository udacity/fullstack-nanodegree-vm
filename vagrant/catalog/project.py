from flask import Flask
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Category, Item

engine = create_engine('postgresql://vagrant:password@localhost:5432/catalogs')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

app = Flask(__name__)


@app.route('/')
@app.route('/catalog/')
def index():
    cat = session.query(Category)
    output = ''
    for c in cat.all():
        output += c.name
        output += '<br>'
    return output


@app.route('/catalog/<category>/items/')
def items(category):
    return 'Welcome to ' + category + ' items!'


@app.route('/catalog/<category>/<item>/')
def item(category, item):
    return 'Welcome %s - %s ' % (category, item)


@app.route('/catalog/<category>/<item>/add')
def add_item():
    return 'Add an item'


@app.route('/catalog/<category>/<item>/edit')
def edit_item():
    return 'Edit an item'


@app.route('/catalog/<category>/<item>/delete')
def delete_item():
    return 'Delete an item'


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0')
