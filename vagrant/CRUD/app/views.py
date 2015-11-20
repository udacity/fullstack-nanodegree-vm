from app import app, db, models, login_manager, forms
from flask import Flask, render_template, request, redirect, jsonify, url_for
from flask import session, flash, abort, g
from sqlalchemy.sql import func, desc, or_
from flask.ext.login import LoginManager, login_user
from flask.ext.login import logout_user, current_user, login_required

import flask.ext.whooshalchemy as whooshalchemy
from forms import SearchForm


def CustomerList():
    customer = models.Customer
    return customer.query.order_by(customer.account_name).\
        group_by(customer.account_name).\
        having(func.max(customer.renewal_date)).all()


def CustomerCountryView():
    customer = models.Customer
    country = models.CustomerCodes
    query = customer.query.order_by(customer.account_name).        group_by(customer.account_name).having(func.max(customer.renewal_date)).        join(country, customer.country_code == country.CODE).        add_columns(customer.account_name, customer.customer_name,        customer.account_id, customer.CustomerNote, country.COUNTRY,        country.SupportRegion, customer.renewal_date, customer.contract_type,        customer.CCGroup).all()  # noqa
    return query


def CustomerCountryPages(page):
    customer = models.Customer
    country = models.CustomerCodes
    query = customer.query.order_by(customer.account_name).\
    group_by(customer.account_name).having(func.max(customer.renewal_date)).\
    join(country, customer.country_code == country.CODE).\
    add_columns(customer.account_name, customer.customer_name,
    customer.account_id, customer.CustomerNote, country.COUNTRY,
    country.SupportRegion, customer.renewal_date, customer.contract_type,
    customer.CCGroup).paginate(page, 50, False)  # noqa
    return query

def CustomerCountryMatch(query, page):
    customer = models.Customer
    country = models.CustomerCodes
    query = customer.query.filter(or_(customer.account_name.match(query),\
    customer.customer_name.match(query))).order_by(customer.account_name).\
    group_by(customer.account_name).having(func.max(customer.renewal_date)).\
    join(country, customer.country_code == country.CODE).\
    add_columns(customer.account_name, customer.customer_name,
    customer.account_id, customer.CustomerNote, country.COUNTRY,
    country.SupportRegion, customer.renewal_date, customer.contract_type,
    customer.CCGroup).paginate(page, 200, False)  # noqa
    return query

def Users():
    users = models.User
    return users.query.order_by(users.registered_on).all()

def getUser(username):
    user = models.User
    return user.query.filter(user.username(username))

@app.route('/')
@app.route('/customers/page/<int:page>')
@login_required
def customerList(page=1):
    customers = CustomerCountryPages(page)
    return render_template('customer_country.html', customers=customers)


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        return render_template('register.html')
    user = models.User(request.form['username'], request.form['password'], request.form['email'])  # noqa
    db.session.add(user)
    db.session.commit()
    flash('User successfully registered')
    return redirect(url_for('login'))


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = forms.LoginForm()
    if form.validate_on_submit():
        login_user(form.user)
        flash(u'Successfully logged in as %s' % form.user.username)
        session['user_id'] = form.user.user_id
        return redirect(url_for('customerList'))
    return render_template('login.html', form=form)


@app.route('/search', methods=['POST'])
@login_required
def search():
    if not g.search_form.validate_on_submit():
        return redirect(url_for('customerList'))
    return redirect(url_for('search_results', query=g.search_form.search.data))

@app.route('/search_results/<query>')
# @app.route('/search_results/page/<int:page>')
@login_required
def search_results(query, page=1):
    results = CustomerCountryMatch(query, page)
    return render_template('search_results.html',
                           query=query,
                           customers=results)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('customerList'))

@app.route('/users')
@login_required
def users():
    if g.user.am_i_admin():
        users = Users()
        print "Heelo users %s", users
        return render_template('userlist.html', users=users)
    return redirect(url_for('customerList'))

@app.route('/edit/user/', methods=['POST', 'GET'])
@login_required
def edit_user(user_id):
    if g.user.am_i_admin():
        user = models.User.query.get(user_id)
        form = forms.EditUser(obj=user)
        print user.username
        #form.populate_obj(user)
        #print form.user.username
        #user.save
        return render_template('edit_user.html', form=form)
    return redirect(url_for('customerList'))

@login_manager.user_loader
def load_user(user_id):
    return models.User.query.get(int(user_id))


@app.before_request
def before_request():
    g.user = current_user
    print "user %s", current_user
    #g.user.is_authenticated = 1
    if g.user.is_authenticated:
        g.search_form = SearchForm()
