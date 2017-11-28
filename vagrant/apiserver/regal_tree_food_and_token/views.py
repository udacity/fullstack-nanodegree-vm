from models import Base, User, Product
from flask import Flask, jsonify, request, url_for, abort, g
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine

from flask_httpauth import HTTPBasicAuth
auth = HTTPBasicAuth()


engine = create_engine('sqlite:///regalTree.db')

Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()
app = Flask(__name__)


#ADD @auth.verify_password decorator here
@auth.verify_password
def verify_password(username_or_token,password):
    #check if the token is provided as username
    print "username_or_token : %s" % username_or_token
    print "password : %s" % password
    user_id = User.verify_auth_token(username_or_token)
    if user_id:
        user = session.query(User).filter_by(id=user_id).one()
    else:
        user = session.query(User).filter_by(username=username_or_token).first()    
        if not user:
            print "User Not Found"
            return False
        elif not user.verify_password(password):
            print "Unable to verify password"
            return False        
    if user:
        g.user = user
        return True                         
    print "User Not Found"
    return False
        
#add /token route here to get a token for a user with login credentials
@app.route('/token')
@auth.login_required
def get_auth_token():
    token = g.user.generate_auth_token()
    return jsonify({'token':token.decode('ascii')})

@app.route('/users', methods = ['POST'])
def new_user():
    username = request.json.get('username')
    password = request.json.get('password')
    if username is None or password is None:
        print "missing arguments"
        abort(400) 
        
    if session.query(User).filter_by(username = username).first() is not None:
        print "existing user"
        user = session.query(User).filter_by(username=username).first()
        return jsonify({'message':'user already exists'}), 201 #, {'Location': url_for('get_user', id = user.id, _external = True)}
        
    user = User(username = username)
    user.hash_password(password)
    session.add(user)
    session.commit()
    return jsonify({ 'username': user.username }), 201 #, {'Location': url_for('get_user', id = user.id, _external = True)}

@app.route('/users/<int:id>')
def get_user(id):
    user = session.query(User).filter_by(id=id).one()
    if not user:
        abort(400)
    return jsonify({'username': user.username})

@app.route('/resource')
@auth.login_required
def get_resource():
    return jsonify({ 'data': 'Hello, %s!' % g.user.username })

@app.route('/products', methods = ['GET', 'POST'])
@auth.login_required
def showAllProducts():
    if request.method == 'GET':
        products = session.query(Product).all()
        return jsonify(products = [p.serialize for p in products])
    if request.method == 'POST':
        name = request.json.get('name')
        category = request.json.get('category')
        price = request.json.get('price')
        newItem = Product(name = name, category = category, price = price)
        session.add(newItem)
        session.commit()
        return jsonify(newItem.serialize)



@app.route('/products/<category>')
@auth.login_required
def showCategoriedProducts(category):
    if category == 'fruit':
        fruit_items = session.query(Product).filter_by(category = 'fruit').all()
        return jsonify(fruit_products = [f.serialize for f in fruit_items])
    if category == 'legume':
        legume_items = session.query(Product).filter_by(category = 'legume').all()
        return jsonify(legume_products = [l.serialize for l in legume_items])
    if category == 'vegetable':
        vegetable_items = session.query(Product).filter_by(category = 'vegetable').all()
        return jsonify(produce_products = [p.serialize for p in produce_items])
    


if __name__ == '__main__':
    app.debug = True
    #app.config['SECRET_KEY'] = ''.join(random.choice(string.ascii_uppercase + string.digits) for x in xrange(32))
    app.run(host='0.0.0.0', port=5000)