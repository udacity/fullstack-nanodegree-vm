from app import db
from app import app
import flask.ext.whooshalchemy as whooshalchemy
from werkzeug.security import generate_password_hash, check_password_hash

db.reflect()


class Customer(db.Model):
    __tablename__ = 'customer'
    __searchable__ = ['account_name', 'account_id', 'customer_name']


class CustomerCodes(db.Model):
    __tablename__ = 'customer_codes'
    __searchable__ = ['COUNTRY', 'SupportRegion']


class User(db.Model):
    __tablename__ = 'user'

    # def __init__(self, username, password, email, can_edit, edit_note, can_create, is_admin):  # noqa
    #     self.username = username
    #     self.set_password(password)
    #     self.email = email
    #     self.registered_on = datetime.utcnow()
    #     self.can_edit = can_edit
    #     self.edit_note = edit_note
    #     self.can_create = can_create
    #     self.is_admin = is_admin

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return unicode(self.user_id)

    def can_i_edit(self):
        return unicode(self.can_edit)

    def can_i_edit_note(self):
        return unicode(self.edit_note)

    def am_i_admin(self):
        return unicode(self.is_admin)
    #
    def can_i_create(self):
        return unicode(self.can_create)

    # def __repr__(self):
    #     return '<User %r>' % (self.username)


whooshalchemy.whoosh_index(app, Customer)
whooshalchemy.whoosh_index(app, CustomerCodes)
