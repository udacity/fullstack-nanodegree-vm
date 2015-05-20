from flask.ext.wtf import Form
from wtforms import TextField
from wtforms.validators import Required
from wtforms.widgets import TextArea


class CategoryForm(Form):
    name = TextField('name', validators=[Required()])
    description = TextField('description',  widget=TextArea())


class ItemForm(Form):
    name = TextField('name', validators=[Required()])
    description = TextField('description', validators=[Required()], widget=TextArea())
