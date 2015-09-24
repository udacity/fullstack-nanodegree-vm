import psycopg2
from flask import Flask, request, session, g, redirect, url_for, \
     abort, render_template

# Configure database
DEBUG = True
SECRET_KEY = 'development-key'

# Default username and passwords
USERNAME = 'admin'
PASSWORD = 'default'

# Configure flask
app = Flask(__name__)
app.config.from_object(__name__)


# Render index page
@app.route("/")
def index():
    return render_template('index.html', categories=get_categories(),  items=get_items())


# Category items
@app.route("/catalog/<category>/items")
def category_items(category):
    # Get items by category
    items = get_items_where_cat(category)
    return render_template(
        'category.html',
        all_categories=get_categories(),
        category=category,
        items=items,
        resno=len(items)
    )


# Item page
@app.route("/catalog/<category>/<item_name>")
def item_desc(category, item_name):
    item = get_items_where_cat_and_name(category, item_name)[0]
    return render_template('item.html', item=item)


# Add item page
@app.route('/add-item', methods=['GET', 'POST'])
def add_item_page():
    if not session.get('logged_in'):
        abort(401)
    else:
        if request.method == 'POST':
            # Get form data
            title = request.form['title']
            category = request.form['category']
            # Add item to database
            add_item(title, category, request.form['descrip'])
            return redirect('/catalog/' + category + '/' + title)
    return render_template(
        'add-item.html',
        all_categories=get_categories(),
        action="/add-item",
        title="Add item",
        title_val="",
        desc_val="",
        cat_val=""
    )


# Add category page
@app.route('/add-category', methods=['GET', 'POST'])
def add_category_page():
    if not session.get('logged_in'):
        abort(401)
    else:
        if request.method == 'POST':
            name = request.form['title']
            # Add category
            add_category(name)
            return redirect('/catalog/' + name + '/items')
    return render_template('add-category.html')


# Edit item page
@app.route('/catalog/<item>/edit', methods=['GET', 'POST'])
def edit_item_page(item):
    action = '/catalog/' + item + '/edit'

    old_title = ""
    old_desc = ""
    old_cat = ""

    if not session.get('logged_in'):
        abort(401)
    else:
        # Get items by name
        query = get_items_where_name(item)
        # Get old values
        old_title = query[0]
        old_cat = query[1]
        old_desc = query[2]
        if request.method == 'POST':
            # Get new values from form
            new_title = request.form['title']
            new_category = request.form['category']
            new_descrip = request.form['descrip']

            # Edit item
            edit_item(old_title, new_title, new_category, new_descrip)
            # Redirect to edited page
            return redirect('/catalog/' + new_category + '/' + new_title)
    return render_template(
        'edit-item.html',
        all_categories=get_categories(),
        action=action,
        title="Edit item",
        title_val=old_title,
        desc_val=old_desc,
        cat_val=old_cat
    )


# Item deletion confirmation page
@app.route('/catalog/<item>/del-confirmation')
def delete_confirmation_page(item):
    return render_template('delete-item.html', item=item)


# Deletes item and redirects to index
@app.route('/catalog/<item>/delete')
def delete_item_page(item):
    if not session.get('logged_in'):
        abort(401)
    else:
        delete_item(item)
    return redirect(url_for('index'))


# Login page
@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != app.config['USERNAME']:
            error = 'Invalid username'
        elif request.form['password'] != app.config['PASSWORD']:
            error = 'Invalid password'
        else:
            session['logged_in'] = True
            return redirect(url_for('index'))
    return render_template('login.html', error=error)


# Logs out and redirects to index
@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    return redirect(url_for('index'))


# Connect to the database
def connect():
    return psycopg2.connect("dbname=catalog")


# Runs a query
def run_query(query):
    if type(query) is list:
        if len(query) >= 3:
            raise ValueError('Query can only contain up to 2 arguments')
    conn = connect()
    c = conn.cursor()
    # If query is just a string
    if type(query) is str:
        c.execute(query)
    # If it's an array, pass second param as data
    else:
        c.execute(query[0], query[1])
    ret = None
    try:
        ret = c.fetchall()
    except psycopg2.ProgrammingError:
        pass
    conn.commit()
    conn.close()
    return ret


''' Below functions handle database interaction '''


# Adds category to the database
def add_category(category_name):
    run_query(["INSERT INTO categories(category) VALUES(%s);", (category_name, )])


# Adds item to db
def add_item(item_name, category, descrip):
    run_query([
        'INSERT INTO items(name, category, descrip) VALUES(%s, %s, %s);',
        (item_name, category, descrip)
    ])


# Edits item
def edit_item(current_name, new_name, category, descrip):
    run_query([
        'UPDATE items SET name=%s, category=%s, descrip=%s WHERE name=%s;',
        (new_name, category, descrip, current_name)
    ])


# Deletes item
def delete_item(item_name):
    run_query(['DELETE FROM items WHERE name=%s;', (item_name,)])


# Gets all categories
def get_categories():
    return run_query("SELECT category FROM categories;")


# Gets all items
def get_items():
    return run_query("SELECT name, category FROM items;")


# Get items by category
def get_items_where_cat(category):
    return run_query([
        "SELECT name, category FROM items WHERE category=%s;",
        (category,)
    ])


# Get items by name
def get_items_where_name(item_name):
    return run_query([
        "SELECT * FROM items WHERE name=%s;",
        (item_name,)
    ])[0]


# Get items by category and name
def get_items_where_cat_and_name(category, item_name):
    return run_query([
        "SELECT * FROM items WHERE category=%s AND name=%s;",
        (category, item_name)
    ])


# Hosts the application
if __name__ == "__main__":
    app.run(host='0.0.0.0')
