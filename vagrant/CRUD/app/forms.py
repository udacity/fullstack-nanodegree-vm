from flask.ext.wtf import Form
from wtforms import BooleanField, StringField, validators
from wtforms import StringField, BooleanField, TextAreaField
from wtforms.validators import DataRequired, Length

class SearchForm(Form):
    search = StringField('search', validators=[DataRequired()])
