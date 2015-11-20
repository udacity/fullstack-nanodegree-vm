from flask.ext.wtf import Form
from wtforms import TextField, StringField, validators
from wtforms import StringField, BooleanField, TextAreaField, PasswordField
from wtforms.validators import DataRequired, Length
from app import app, models


class SearchForm(Form):
    search = StringField('search', validators=[DataRequired()])

class RegistrationForm(Form):
    username     = StringField('Username', [validators.Length(min=4, max=25)])
    email        = StringField('Email Address', [validators.Length(min=6, max=35)])
    fullName    = StringField('Full Name', [validators.Length(min=4, max=50)])
    password = PasswordField('Password')


class ProfileForm(Form):
    username     = StringField('Username', [validators.Length(min=4, max=25)])
    email        = StringField('Email Address', [validators.Length(min=6, max=35)])
    fullName    = StringField('Full Name', [validators.Length(min=4, max=50)])
    password = PasswordField('Password')


class EditUser(Form):
    username     = StringField('Username', [validators.Length(min=4, max=25)])
    email        = StringField('Email Address', [validators.Length(min=6, max=35)])
    fullname    = StringField('Full Name', [validators.Length(min=4, max=50)])
    password = PasswordField('Password')
    can_edit = BooleanField('Can Edit Customers')
    edit_note = BooleanField('Can Edit Customer Note')
    can_create = BooleanField('Can Create Customers')
    is_admin = BooleanField('Can Edit Everything')

class LoginForm(Form):
    username = TextField('Username', [validators.Required()])
    password = PasswordField('Password', [validators.Required()])

    def __init__(self, *args, **kwargs):
        Form.__init__(self, *args, **kwargs)
        self.user = None

    def validate(self):
        rv = Form.validate(self)
        if not rv:
            return False
        user = models.User.query.filter_by(
            username=self.username.data).first()
        if user is None:
            self.username.errors.append('Unknown username')
            return False

        if not user.check_password(self.password.data):
            self.password.errors.append('Invalid password')
            return False

        self.user = user
        return True
