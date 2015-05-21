import os
basedir = os.path.abspath(os.path.dirname(__file__))

CSRF_ENABLED = True
SECRET_KEY = 'you-will-never-guess'
UPLOADED_IMAGES_DEST = os.path.join(basedir, 'app/static/uploads')
