from app import db
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash

db.reflect()

class Customer(db.Model):
    #__bind_key__ = 'None'
    __tablename__ = 'customer'


class CustomerCodes(db.Model):
    #__bind_key__ = 'None'
    __tablename__ = 'customer_codes'

class User(db.Model):
    __tablename__ = 'user'

    def __init__(self , username ,password , email):
        self.username = username
        self.set_password(password)
        self.email = email
        self.registered_on = datetime.utcnow()

    def set_password(self , password):
        self.password = generate_password_hash(password)

    def check_password(self , password):
        return check_password_hash(self.password , password)

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return unicode(self.user_id)

    def __repr__(self):
        return '<User %r>' % (self.username)
