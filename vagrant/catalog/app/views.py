from flask import render_template, request, url_for, redirect, flash
from forms import CategoryForm, ItemForm, DeleteForm, images
from models import Category, Item
from database import db_session
from app import app
from sqlalchemy.exc import IntegrityError


def flash_errors(form):
    """Snippet from http://flask.pocoo.org/snippets/12/"""
    for field, errors in form.errors.items():
        for error in errors:
            flash(u"Error in the %s field - %s" % (
                getattr(form, field).label.text,
                error
            ))


@app.context_processor
def inject_categories():
    """Inject categories in all views"""
    return dict(categories=Category.query.all())


@app.route('/')
def index():
    """Basic view, that grab last five items"""
    items = Item.query.order_by(Item.id.desc()).limit(5)
    return render_template('index.html',
                           items=items)


@app.route('/catalog/new', methods=['GET'])
def category_create():
    """Create category with WTFForm"""
    form = CategoryForm()
    return render_template('category/create.html',
                           form=form)


@app.route('/catalog', methods=['POST'])
def category_store():
    """Store new category, check for database & forms error"""
    form = CategoryForm()
    if form.validate_on_submit():
        try:
            new_category = Category(form.name.data, form.description.data)
            db_session.add(new_category)
            db_session.commit()
            return redirect(url_for('category_view',
                                    category_name=form.name.data))
        except IntegrityError:
            db_session.rollback()
            flash("Category name must be unique value")
        except Exception:
            db_session.rollback()
            flash("Database error encountered")
    flash_errors(form)
    return redirect(url_for('category_create'))


@app.route('/catalog/<category_name>', methods=['GET'])
def category_view(category_name):
    """View category with his items"""
    category = Category.query.\
        filter(Category.name == category_name).\
        first()
    return render_template('category/view.html',
                           category=category)


@app.route('/catalog/<category_name>/edit', methods=['GET'])
def category_edit(category_name):
    """Edit category name and description method
        and button for delete"""
    form = CategoryForm()
    delete_form = DeleteForm()
    category = Category.query.filter(Category.name == category_name).first()
    form.name.data = category.name
    form.description.data = category.description
    return render_template('category/edit.html',
                           category=category,
                           form=form,
                           delete_form=delete_form)


@app.route('/catalog/<category_name>/update', methods=['POST'])
def category_update(category_name):
    """Update category name and description in database"""
    form = CategoryForm()
    if form.validate_on_submit():
        try:
            category = Category.query.filter(Category.name == category_name).first()
            category.name = form.name.data
            category.description = form.description.data
            db_session.add(category)
            db_session.commit()
            return redirect(url_for('category_view',
                                    category_name=form.name.data))
        except IntegrityError:
            db_session.rollback()
            flash("Category name must be unique value")
        except Exception:
            db_session.rollback()
            flash("Database error encountered")
    flash_errors(form)
    return redirect(url_for('category_edit',
                            category_name=category_name))


@app.route('/catalog/<category_name>/delete', methods=['POST'])
def category_delete(category_name):
    delete_form = DeleteForm()
    if delete_form.validate_on_submit():
        category = Category.query.filter(Category.name == category_name).first()
        db_session.delete(category)
        db_session.commit()
        return redirect(url_for('index'))
    flash_errors(delete_form)
    return redirect(url_for('category_edit',
                            category_name=category_name))


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
    form.category_id.choices = [(c.id, c.name) for c in Category.query.order_by('name')]
    category = Category.query.filter(Category.name == category_name).first()
    form.category_id.data = category.id
    if form.validate_on_submit():
        try:
            new_item = Item(form.name.data,
                            form.description.data,
                            category.id)
            if 'image' in request.files and request.files['image']:
                filename = images.save(request.files['image'])
                new_item.image_name = filename
            db_session.add(new_item)
            db_session.commit()
            return redirect(url_for('item_view',
                                    category_name=category_name,
                                    item_name=form.name.data))
        except IntegrityError:
            db_session.rollback()
            flash("Item name must be unique value")
        except Exception, e:
            db_session.rollback()
            print e
            flash("Database error encountered")
    flash_errors(form)
    return redirect(url_for('item_create', category_name=category_name))


@app.route('/catalog/<category_name>/item/<item_name>', methods=['GET'])
def item_view(category_name, item_name):
    item = Item.query.\
        filter(Item.name == item_name).\
        filter(Item.category.has(name=category_name)).\
        first()
    return render_template('item/view.html',
                           item=item,
                           category_name=category_name)


@app.route('/catalog/<category_name>/item/<item_name>/edit', methods=['GET'])
def item_edit(category_name, item_name):
    form = ItemForm()
    form.category_id.choices = [(c.id, c.name) for c in Category.query.order_by('name')]
    delete_form = DeleteForm()
    item = Item.query.\
        filter(Item.name == item_name).\
        filter(Item.category.has(name=category_name)).\
        first()
    form.name.data = item.name
    form.description.data = item.description
    form.category_id.data = item.category_id
    return render_template('item/edit.html',
                           item=item,
                           category_name=category_name,
                           form=form,
                           delete_form=delete_form)


@app.route('/catalog/<category_name>/item/<item_name>/update', methods=['POST'])
def item_update(category_name, item_name):
    form = ItemForm()
    form.category_id.choices = [(c.id, c.name) for c in Category.query.order_by('name')]
    if form.validate_on_submit():
        try:
            item = Item.query.\
                filter(Item.name == item_name).\
                filter(Item.category.has(name=category_name)).\
                first()
            category = Category.query.filter(Category.id == form.category_id.data).first()
            item.name = form.name.data
            item.description = form.description.data
            item.category_id = form.category_id.data
            if 'image' in request.files and request.files['image']:
                filename = images.save(request.files['image'])
                item.image_name = filename
            db_session.add(item)
            db_session.commit()
            return redirect(url_for('item_view',
                                    category_name=category.name,
                                    item_name=form.name.data))
        except IntegrityError:
            db_session.rollback()
            flash("Item name must be unique value")
        except Exception:
            db_session.rollback()
            flash("Database error encountered")
    flash_errors(form)
    return redirect(url_for('item_edit',
                            category_name=category_name,
                            item_name=form.name.data))


@app.route('/catalog/<category_name>/item/<item_name>/delete', methods=['POST'])
def item_delete(category_name, item_name):
    delete_form = DeleteForm()
    if delete_form.validate_on_submit():
        item = Item.query.filter(Item.category.has(name=category_name)).first()
        db_session.delete(item)
        db_session.commit()
        return redirect(url_for('index'))
    flash_errors(delete_form)
    return redirect(url_for('item_edit',
                            category_name=category_name,
                            item_name=form.name.data))
