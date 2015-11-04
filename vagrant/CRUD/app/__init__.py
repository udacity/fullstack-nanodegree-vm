from wtforms import Form, BooleanField, StringField, validators
from flask import Flask, render_template, request, redirect, jsonify, url_for
from flask import session, flash, abort, g
from flask.ext.sqlalchemy import SQLAlchemy, Pagination
from sqlalchemy.sql import func, desc
from flask.ext.login import LoginManager, login_user
from flask.ext.login import logout_user, current_user, login_required


app = Flask(__name__)
app.config.from_pyfile('config.py')

db = SQLAlchemy(app)
from app import models, views
login_manager = LoginManager()
login_manager.init_app(app)


login_manager.login_view = 'login'
@app.before_request
def before_request():
    g.user = current_user

@app.route('/')

#@app.route('/customers/,defaults{'page':1})
@app.route('/customers/page/<int:page>')
def customerList(page=1):
    customers = views.CustomerCountryPages(page)
    # customer_dict = dict((col, getattr(customer, col)) for col in customer.__table__.columns.keys())  # noqa
    #customer = customers.paginate(1, 50, False).items
    #return jsonify(result=list(customers))
    return render_template('customer_country.html', customers=customers)

@app.route('/register' , methods=['GET','POST'])
def register():
    if request.method == 'GET':
        return render_template('register.html')
    user = User(request.form['username'] , request.form['password'],request.form['email'])
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
    registered_user = User.query.filter_by(username=username,password=password).first()
    if registered_user is None:
        flash('Username or Password is invalid' , 'error')
        return redirect(url_for('login'))
    login_user(registered_user)
    flash('Logged in successfully')
    return redirect(request.args.get('next') or url_for('index'))

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))
