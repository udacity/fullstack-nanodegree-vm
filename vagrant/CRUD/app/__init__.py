from datetime import datetime
from wtforms import Form, BooleanField, StringField, validators
from flask import Flask, render_template, request, redirect, jsonify, url_for
from flask import session, flash, abort, g
from flask.ext.sqlalchemy import SQLAlchemy, Pagination
from sqlalchemy.sql import func, desc
from flask.ext.login import LoginManager, login_user
from flask.ext.login import logout_user, current_user, login_required
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.config.from_pyfile('config.py')

db = SQLAlchemy(app)
from app import models, views
login_manager = LoginManager()
login_manager.init_app(app)

login_manager.login_view = 'login'

@app.route('/')
@app.route('/customers/page/<int:page>')
@login_required
def customerList(page=1):
    customers = views.CustomerCountryPages(page)
    # customer_dict = dict((col, getattr(customer, col)) for col in customer.__table__.columns.keys())  # noqa
    #customer = customers.paginate(1, 50, False).items
    #return jsonify(result=list(customers))
    return render_template('customer_country.html', customers=customers)

@app.route('/register', methods=['GET','POST'])
def register():
    if request.method == 'GET':
        return render_template('register.html')
    user = models.User(request.form['username'] , request.form['password'],request.form['email'])
    db.session.add(user)
    db.session.commit()
    flash('User successfully registered')
    return redirect(url_for('login'))

@app.route('/login',methods=['GET','POST'])
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
        flash('Username is invalid' , 'error')
        return redirect(url_for('login'))
    if not registered_user.check_password(password):
        flash('Password is invalid','error')
        return redirect(url_for('login'))
    login_user(registered_user, remember = remember_me)
    flash('Logged in successfully')
    return redirect(url_for('customerList'))

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
    #if 'logged_in' not in session and request.endpoint not in ('login', 'static', 'register'):
    #    return redirect(url_for('login'))

#    print 'current_user: %s, g.user: %s, leaving bef_req' % (current_user, g.user)
