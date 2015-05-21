from flask import Flask, url_for

app = Flask(__name__)
app.config.from_object('config')

# Function to easily find your assets
# In your template use <link rel=stylesheet href="{{ static('filename') }}">
app.jinja_env.globals['static'] = (
    lambda filename: url_for('static', filename=filename)
)


from app import views
