from flask import render_template, request, url_for, redirect
from forms import CategoryForm, ItemForm
from models import Category, Item
from database import db_session
from app import app

# Inject categories in all views


@app.context_processor
def inject_categories():
    return dict(categories=Category.query.all())


# Basic view

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
    form = CategoryForm()
    if form.validate_on_submit():
        new_category = Category(form.name.data, form.description.data)
        db_session.add(new_category)
        db_session.commit()
        return redirect(url_for('category_view',
                                category_name=form.name.data))


@app.route('/catalog/<category_name>', methods=['GET'])
def category_view(category_name):
    category = Category.query.\
        filter(Category.name == category_name).\
        first()
    return render_template('category/view.html',
                           category=category)


@app.route('/catalog/<category_name>/edit', methods=['GET'])
def category_edit(category_name):
    form = CategoryForm()
    category = Category.query.filter(Category.name == category_name).first()
    form.name.data = category.name
    form.description.data = category.description
    return render_template('category/edit.html',
                           category=category,
                           form=form)


@app.route('/catalog/<category_name>/update', methods=['POST'])
def category_update(category_name):
    form = CategoryForm()
    if form.validate_on_submit():
        category = Category.query.filter(Category.name == category_name).first()
        category.name = form.name.data
        category.description = form.description.data
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


@app.route('/catalog/<category_name>/item/new', methods=['GET'])
def item_create(category_name):
    form = ItemForm()
    return render_template('item/create.html',
                           form=form,
                           category_name=category_name)


@app.route('/catalog/<category_name>/item', methods=['POST'])
def item_store(category_name):
    form = ItemForm()
    if form.validate_on_submit():
        category = Category.query.filter(Category.name == category_name).one()
        new_item = Item(form.name.data,
                        form.description.data,
                        'Test',
                        category.id)
        db_session.add(new_item)
        db_session.commit()
        return redirect(url_for('item_view',
                                category_name=category_name,
                                item_name=form.name.data))
    return 'fail'


@app.route('/catalog/<category_name>/item/<item_name>', methods=['GET'])
def item_view(category_name, item_name):
    item = Item.query.filter(Item.category.has(name=category_name)).one()
    return render_template('item/view.html',
                           item=item)


@app.route('/catalog/<category_name>/item/<item_name>/edit', methods=['GET'])
def item_edit(category_name, item_name):
    item = Item.query.filter(Item.category.has(name=category_name)).one()
    return render_template('category/edit.html',
                           item=item)


@app.route('/catalog/<category_name>/item/<item_name>/update', methods=['POST'])
def item_update(category_name, item_name):
    form = CategoryForm(request.form)
    form.category_id.choices = [(c.id, c.name) for c in Category.query.order_by('name')]
    item = Item.query.filter(Item.category.has(name=category_name)).one()
    category = Category.query.filter(Category.id == form.category_id.data).one()
    db_session.add(item)
    db_session.commit()
    return redirect(url_for('item_view',
                            category_name=category.name,
                            item_name=form.name.data))


@app.route('/catalog/<category_name>/item/<item_name>/delete', methods=['POST'])
def item_delete(category_name, item_name):
    item = Item.query.filter(Item.category.has(name=category_name)).one()
    db_session.delete(item)
    db_session.commit()
    return redirect(url_for('index'))
