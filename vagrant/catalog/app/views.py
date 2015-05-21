from flask import render_template, request, url_for, redirect, flash
from forms import CategoryForm, ItemForm, DeleteForm, images
from models import Category, Item, User
from database import db_session
from app import app
from sqlalchemy.exc import IntegrityError
from oauth2client.client import flow_from_clientsecrets
from oauth2client.client import FlowExchangeError
from flask import session as login_session
from flask import make_response
import random
import string
import httplib2
import json
import requests


CLIENT_ID = '261874505746-c2qvcgtn95o8v20hribca3osa39s1vkt.apps.googleusercontent.com'


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
    state = ''.join(random.choice(string.ascii_uppercase + string.digits) for x in xrange(32))
    login_session['state'] = state
    return render_template('index.html',
                           items=items,
                           STATE=state)


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
                            item_name=item_name))


@app.route('/gconnect', methods=['POST'])
def gconnect():
    # Validate state token
    if request.args.get('state') != login_session['state']:
        response = make_response(json.dumps('Invalid state parameter.'), 401)
        response.headers['Content-Type'] = 'application/json'
        return response
    # Obtain authorization code
    code = request.data

    try:
        # Upgrade the authorization code into a credentials object
        oauth_flow = flow_from_clientsecrets('client_secrets.json', scope='')
        oauth_flow.redirect_uri = 'postmessage'
        credentials = oauth_flow.step2_exchange(code)
    except FlowExchangeError:
        response = make_response(
            json.dumps('Failed to upgrade the authorization code.'), 401)
        response.headers['Content-Type'] = 'application/json'
        return response

    # Check that the access token is valid.
    access_token = credentials.access_token
    url = ('https://www.googleapis.com/oauth2/v1/tokeninfo?access_token=%s'
           % access_token)
    h = httplib2.Http()
    result = json.loads(h.request(url, 'GET')[1])
    # If there was an error in the access token info, abort.
    if result.get('error') is not None:
        response = make_response(json.dumps(result.get('error')), 500)
        response.headers['Content-Type'] = 'application/json'

    # Verify that the access token is used for the intended user.
    gplus_id = credentials.id_token['sub']
    if result['user_id'] != gplus_id:
        response = make_response(
            json.dumps("Token's user ID doesn't match given user ID."), 401)
        response.headers['Content-Type'] = 'application/json'
        return response

    # Verify that the access token is valid for this app.
    if result['issued_to'] != CLIENT_ID:
        response = make_response(
            json.dumps("Token's client ID does not match app's."), 401)
        print "Token's client ID does not match app's."
        response.headers['Content-Type'] = 'application/json'
        return response

    stored_credentials = login_session.get('credentials')
    stored_gplus_id = login_session.get('gplus_id')
    if stored_credentials is not None and gplus_id == stored_gplus_id:
        response = make_response(json.dumps('Current user is already connected.'),
                                 200)
        response.headers['Content-Type'] = 'application/json'
        return response

    # Store the access token in the session for later use.
    login_session['credentials'] = credentials
    login_session['gplus_id'] = gplus_id

    # Get user info
    userinfo_url = "https://www.googleapis.com/oauth2/v1/userinfo"
    params = {'access_token': credentials.access_token, 'alt': 'json'}
    answer = requests.get(userinfo_url, params=params)

    data = answer.json()

    login_session['username'] = data['name']
    login_session['picture'] = data['picture']
    login_session['email'] = data['email']
    # ADD PROVIDER TO LOGIN SESSION
    login_session['provider'] = 'google'

    # see if user exists, if it doesn't make a new one
    user_id = getUserID(data["email"])
    if not user_id:
        user_id = createUser(login_session)
    login_session['user_id'] = user_id

    output = ''
    output += '<h1>Welcome, '
    output += login_session['username']
    output += '!</h1>'
    output += '<img src="'
    output += login_session['picture']
    output += ' " style = "width: 300px; height: 300px;border-radius: 150px;-webkit-border-radius: 150px;-moz-border-radius: 150px;"> '
    flash("you are now logged in as %s" % login_session['username'])
    print "done!"
    return output

# User Helper Functions


def createUser(login_session):
    newUser = User(name=login_session['username'], email=login_session[
                   'email'], picture=login_session['picture'])
    db_session.add(newUser)
    db_session.commit()
    user = User.query.filter_by(email=login_session['email']).one()
    return user.id


def getUserInfo(user_id):
    user = User.query.filter_by(id=user_id).one()
    return user


def getUserID(email):
    try:
        user = User.query.filter_by(email=email).one()
        return user.id
    except:
        return None

# DISCONNECT - Revoke a current user's token and reset their login_session


@app.route('/gdisconnect')
def gdisconnect():
    # Only disconnect a connected user.
    credentials = login_session.get('credentials')
    if credentials is None:
        response = make_response(
            json.dumps('Current user not connected.'), 401)
        response.headers['Content-Type'] = 'application/json'
        return response
    access_token = credentials.access_token
    url = 'https://accounts.google.com/o/oauth2/revoke?token=%s' % access_token
    h = httplib2.Http()
    result = h.request(url, 'GET')[0]
    if result['status'] != '200':
        # For whatever reason, the given token was invalid.
        response = make_response(
            json.dumps('Failed to revoke token for given user.', 400))
        response.headers['Content-Type'] = 'application/json'
        return response
