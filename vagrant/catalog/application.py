from flask import Flask, render_template, request, redirect
from db import Category, Item, DBSession

app = Flask(__name__, static_url_path="/static")

def get_all_categories():
    session = DBSession()
    categories = session.query(Category).order_by(Category.name).all()
    session.close()
    return categories


@app.route('/')
def main():
    return render_template('main.html', categories=get_all_categories())

# @TODO - make sure accepts a category slug 
@app.route('/category')
def category():
    return render_template('category.html')

# @TODO - make sure accepts a item slug 
@app.route('/item')
def item():
    return render_template('item.html')

@app.route('/item/new', methods=['GET', 'POST'])
def create_item():
    if request.method == 'GET':
        return render_template('new-item.html', categories=get_all_categories())
    else:
        name = request.form['name']
        description = request.form['description']
        category_id = request.form['category']

        session = DBSession()
        new_item = Item(name=name, description=description, category_id=category_id)
        session.add(new_item)
        session.commit()
        session.close()

        return redirect('/', code=303)


if __name__ == '__main__':
    # @TODO - remove debug mode
    app.run(host='0.0.0.0', port=8000, debug=True)

