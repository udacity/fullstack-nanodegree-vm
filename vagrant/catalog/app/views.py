from flask import render_template, request, url_for, redirect
from forms import CategoryForm
from models import Category
from database import db_session
from app import app


@app.route('/')
def index():
    return render_template('index.html')

# CRUD for categories


@app.route('/catalog', methods=['GET'])
def category_index():
    return render_template('index.html')


@app.route('/catalog/new', methods=['GET'])
def category_create():
    form = CategoryForm()
    return render_template('category/create.html',
                           form=form)


@app.route('/catalog', methods=['POST'])
def category_store():
    form = CategoryForm(request.form)
    new_category = Category(form.name.data, 'Test')
    db_session.add(new_category)
    db_session.commit()
    return redirect(url_for('category_view',
                            category_name=form.name.data))


@app.route('/catalog/<category_name>', methods=['GET'])
def category_view(category_name):
    category = Category.query.filter(Category.name == category_name).first()
    return render_template('category/view.html',
                           category=category)


@app.route('/catalog/<category_name>/edit', methods=['GET'])
def category_edit(category_name):
    category = Category.query.filter(Category.name == category_name).first()
    return render_template('category/edit.html',
                           category=category)


@app.route('/catalog/<category_name>/update', methods=['POST'])
def category_update(category_name):
    form = CategoryForm(request.form)
    category = Category.query.filter(Category.name == category_name).first()
    db_session.add(category)
    db_session.commit()
    return redirect(url_for('category_view',
                            category_name=form.name.data))


@app.route('/catalog/<category_name>/delete', methods=['POST'])
def category_delete(category_name):
    category = Category.query.filter(Category.name == category_name).first()
    db_session.delete(category)
    db_session.commit()
    return redirect(url_for('index'))


# CRUD for items


@app.route('/item/new', methods=['GET'])
def item_create():
    return render_template('index.html')


@app.route('/item', methods=['POST'])
def item_store():
    return render_template('index.html')


@app.route('/catalog/<category_name>/item/<item_name>', methods=['GET'])
def item_view(category_name, item_name):
    return render_template('index.html')


@app.route('/catalog/<category_name>/item/<item_name>/edit', methods=['GET'])
def item_edit(category_name, item_name):
    return render_template('index.html')


@app.route('/catalog/<category_name>/item/<item_name>/update', methods=['POST'])
def item_update(category_name, item_name):
    return render_template('index.html')


@app.route('/catalog/<category_name>/item/<item_name>/delete', methods=['POST'])
def item_delete(category_name, item_name):
    return render_template('index.html')
