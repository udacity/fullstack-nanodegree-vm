from flask import Flask, url_for

catalog = Flask(__name__)

# Function to easily find your assets
# In your template use <link rel=stylesheet href="{{ static('filename') }}">
catalog.jinja_env.globals['static'] = (
    lambda filename: url_for('static', filename=filename)
)

from catalog import views
