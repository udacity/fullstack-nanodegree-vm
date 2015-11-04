from app import db


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
        self.password = password
        self.email = email
        self.registered_on = datetime.utcnow()

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return unicode(self.id)

    def __repr__(self):
        return '<User %r>' % (self.username)
