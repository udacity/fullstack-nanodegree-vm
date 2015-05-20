from flask.ext.wtf import Form
from wtforms import TextField, SelectField
from wtforms.validators import Required


class CategoryForm(Form):
    name = TextField('name', validators=[Required()])
    description = TextField('description', validators=[Required()])


class ItemForm(Form):
    name = TextField('name', validators=[Required()])
    description = TextField('description', validators=[Required()])
    category_id = SelectField(u'Group', coerce=int)
