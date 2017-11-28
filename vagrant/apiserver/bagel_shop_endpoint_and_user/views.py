from models import Base, User, Bagel
from flask import Flask, jsonify, request, url_for, abort, g
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine
from flask_httpauth import HTTPBasicAuth

auth = HTTPBasicAuth() 


engine = create_engine('sqlite:///bagelShop.db')

Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()
app = Flask(__name__)

#ADD @auth.verify_password here
@auth.verify_password
def verify_password(username,password):
    user = session.query(User).filter_by(username=username).first()
    if not user:
        print "User Not Found"
        return False
    elif not user.verify_password(password):
        print "Unable to verify password"
        return False
    else:        
        g.user = user
        return True    

#ADD a /users route here
@app.route('/users', methods = ['POST'])
def new_user():
    username = request.json.get('username')    
    password = request.json.get('password')
    if username is None or password is None:
        abort(400) # Mandatory inputs are missing
    user = session.query(User).filter_by(username=username).first()    
    if user is not None:
        print "Existing User"
        return jsonify({'message' : 'User is allredy registered'}), 201
    newUser = User(username=username)
    newUser.hash_password(password)
    session.add(newUser)
    session.commit()    
    return jsonify({'username' : newUser.username}), 201

# @app.route('/protected_data')
# @auth.login_required
# def get_data():
#     return jasonify({'data': 'Hello %s : ' % g.user.username })

@app.route('/bagels', methods = ['GET','POST'])
@auth.login_required
#protect this route with a required login
def showAllBagels():
    if request.method == 'GET':
        bagels = session.query(Bagel).all()
        return jsonify(bagels = [bagel.serialize for bagel in bagels])
    elif request.method == 'POST':
        name = request.json.get('name')
        description = request.json.get('description')
        picture = request.json.get('picture')
        price = request.json.get('price')
        newBagel = Bagel(name = name, description = description, picture = picture, price = price)
        session.add(newBagel)
        session.commit()
        return jsonify(newBagel.serialize)



if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5000)
