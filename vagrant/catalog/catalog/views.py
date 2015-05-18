from flask import render_template
from catalog import catalog

@catalog.route('/')
def index():
    return render_template('index.html')
