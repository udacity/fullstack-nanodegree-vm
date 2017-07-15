from flask import Flask, render_template, request, redirect
from db import Category, Item, DBSession
from sqlalchemy import desc

app = Flask(__name__, static_url_path="/static")
session = DBSession()

def get_all_categories():
    return session.query(Category).order_by(Category.name).all()

def get_recent_items():
    return session.query(Item).order_by(desc(Item.created_at)).all()

def get_category_by_id(id):
    return session.query(Category).filter(Category.id == id).first()

def get_item_by_id(id):
    return session.query(Item).filter(Item.id == id).first()


@app.route('/')
def main():
    return render_template('main.html', categories=get_all_categories(), items=get_recent_items())

# TODO - cateogry and item pages should perhaps takes slugs instead of ids at some point
@app.route('/category/<int:category_id>')
def category(category_id):
    return render_template('category.html', categories=get_all_categories(), category=get_category_by_id(category_id))

@app.route('/item/<int:item_id>')
def item(item_id):
    return render_template('item.html', item=get_item_by_id(item_id))

@app.route('/item/new', methods=['GET', 'POST'])
def create_item():
    if request.method == 'GET':
        return render_template('new-item.html', categories=get_all_categories())
    else:
        name = request.form['name']
        description = request.form['description']
        category_id = request.form['category']

        # @TOOD - return errors if name or category is empty

        session = DBSession()
        new_item = Item(name=name, description=description, category_id=category_id)
        session.add(new_item)
        session.commit()
        session.close()

        return redirect('/', code=303)


if __name__ == '__main__':
    # @TODO - remove debug mode
    app.run(host='0.0.0.0', port=8000, debug=True)

