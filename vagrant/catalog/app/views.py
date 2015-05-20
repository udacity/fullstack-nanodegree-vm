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
    categories = Category.query.all()
    return render_template('index.html',
                           categories=categories)

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
    category = Category.query.\
        join(Category.items).\
        filter(Category.name == category_name).\
        first()
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
    form = ItemForm()
    form.category_id.choices = [(c.id, c.name) for c in Category.query.order_by('name')]
    return render_template('item/create.html',
                           form=form)


@app.route('/item', methods=['POST'])
def item_store():
    form = ItemForm()
    form.category_id.choices = [(c.id, c.name) for c in Category.query.order_by('name')]
    if form.validate_on_submit():
        new_category = Item(form.name.data,
                            form.name.description,
                            'Test',
                            form.category_id.data)
        db_session.add(new_category)
        db_session.commit()
        category = Category.query.filter(Category.id == form.category_id.data).first()
        return redirect(url_for('item_view',
                                category_name=category.name,
                                item_name=form.name.data))
    return 'fail'


@app.route('/catalog/<category_name>/item/<item_name>', methods=['GET'])
def item_view(category_name, item_name):
    item = Item.query.filter(Item.category.has(name=category_name)).first()
    return render_template('item/view.html',
                           item=item)


@app.route('/catalog/<category_name>/item/<item_name>/edit', methods=['GET'])
def item_edit(category_name, item_name):
    item = Item.query.filter(Item.category.has(name=category_name)).first()
    return render_template('category/edit.html',
                           item=item)


@app.route('/catalog/<category_name>/item/<item_name>/update', methods=['POST'])
def item_update(category_name, item_name):
    form = CategoryForm(request.form)
    form.category_id.choices = [(c.id, c.name) for c in Category.query.order_by('name')]
    item = Item.query.filter(Item.category.has(name=category_name)).first()
    category = Category.query.filter(Category.id == form.category_id.data).first()
    db_session.add(item)
    db_session.commit()
    return redirect(url_for('item_view',
                            category_name=category.name,
                            item_name=form.name.data))


@app.route('/catalog/<category_name>/item/<item_name>/delete', methods=['POST'])
def item_delete(category_name, item_name):
    item = Item.query.filter(Item.category.has(name=category_name)).first()
    db_session.delete(item)
    db_session.commit()
    return redirect(url_for('index'))
