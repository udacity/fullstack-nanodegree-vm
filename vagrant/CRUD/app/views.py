from app import app, db, models, login_manager
from flask import Flask, render_template, request, redirect, jsonify, url_for
from flask import session, flash, abort, g
from sqlalchemy.sql import func, desc, or_
from flask.ext.login import LoginManager, login_user
from flask.ext.login import logout_user, current_user, login_required
from werkzeug.security import generate_password_hash, check_password_hash
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
    query = customer.query.filter(or_(customer.account_name.match(query))).filter(or_(customer.customer_name.match(query))).order_by(customer.account_name).\
    group_by(customer.account_name).having(func.max(customer.renewal_date)).\
    join(country, customer.country_code == country.CODE).\
    add_columns(customer.account_name, customer.customer_name,
    customer.account_id, customer.CustomerNote, country.COUNTRY,
    country.SupportRegion, customer.renewal_date, customer.contract_type,
    customer.CCGroup).paginate(page, 50, False)  # noqa
    return query

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
    if request.method == 'GET':
        return render_template('login.html')

    username = request.form['username']
    password = request.form['password']
    remember_me = False
    if 'remember_me' in request.form:
        remember_me = True
    registered_user = models.User.query.filter_by(username=username).first()
    if registered_user is None:
        flash('Username is invalid', 'error')
        return redirect(url_for('login'))
    if not registered_user.check_password(password):
        flash('Password is invalid', 'error')
        return redirect(url_for('login'))
    login_user(registered_user, remember=remember_me)
    flash('Logged in successfully')
    return redirect(url_for('customerList'))


@app.route('/search', methods=['POST'])
@login_required
def search():
    if not g.search_form.validate_on_submit():
        return redirect(url_for('customerList'))
    return redirect(url_for('search_results', query=g.search_form.search.data))

@app.route('/search_results/<query>')
@login_required
def search_results(query, page=1):
    print "hello %s" % query
    results = CustomerCountryMatch(query, page)
    print results
    return render_template('search_results.html',
                           query=query,
                           customers=results)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('customerList'))


@login_manager.user_loader
def load_user(id):
    print id

    return models.User.query.get(int(id))


@app.before_request
def before_request():
    g.user = current_user
    if g.user.is_authenticated:
        g.search_form = SearchForm()
