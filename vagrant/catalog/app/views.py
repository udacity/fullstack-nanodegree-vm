from flask import render_template
from app import app


@app.route('/')
def index():
    return render_template('index.html')

# CRUD for categories


@app.route('/catalog', methods=['GET'])
def category_index():
    return render_template('index.html')


@app.route('/catalog/new', methods=['GET'])
def category_create():
    return render_template('index.html')


@app.route('/catalog', methods=['POST'])
def category_store():
    return render_template('index.html')


@app.route('/catalog/<category_name>', methods=['GET'])
def category_view():
    return render_template('index.html')


@app.route('/catalog/<category_name>/edit', methods=['GET'])
def category_edit():
    return render_template('index.html')


@app.route('/catalog/<category_name>/update', methods=['POST'])
def category_update():
    return render_template('index.html')


@app.route('/catalog/<category_name>/delete', methods=['POST'])
def category_delete():
    return render_template('index.html')


# CRUD for items


@app.route('/catalog/<category_name>/item/<item_name>/new', methods=['GET'])
def item_create():
    return render_template('index.html')


@app.route('/catalog/<category_name>/item', methods=['POST'])
def item_store():
    return render_template('index.html')


@app.route('/catalog/<category_name>/item/<item_name>', methods=['GET'])
def item_view():
    return render_template('index.html')


@app.route('/catalog/<category_name>/item/<item_name>/edit', methods=['GET'])
def item_edit():
    return render_template('index.html')


@app.route('/catalog/<category_name>/item/<item_name>/update', methods=['POST'])
def item_update():
    return render_template('index.html')


@app.route('/catalog/<category_name>/item/<item_name>/delete', methods=['POST'])
def item_delete():
    return render_template('index.html')
