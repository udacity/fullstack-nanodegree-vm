from flask.ext.wtf import Form
from wtforms import TextField, SelectField
from wtforms.validators import Required
from wtforms.widgets import TextArea
from flask_wtf.file import FileField, FileAllowed
from flask.ext.uploads import UploadSet, IMAGES, configure_uploads
from app import app

# Configure Flask-Uploads to grab only images
images = UploadSet('images', IMAGES)
configure_uploads(app, (images,))


class CategoryForm(Form):
    """It's class to generate form for creating/updating category"""
    name = TextField('name', validators=[Required()])
    description = TextField('description',  widget=TextArea())


class ItemForm(Form):
    """It's class to generate form for creating/updating item"""
    name = TextField('name', validators=[Required()])
    description = TextField('description',
                            validators=[Required()],
                            widget=TextArea())
    image = FileField('image', validators=[
        FileAllowed(images, 'You can upload only images')
    ])
    category_id = SelectField('category', coerce=int)


class DeleteForm(Form):
    """This class is used for creating delete form with CRSF Token"""
    pass
