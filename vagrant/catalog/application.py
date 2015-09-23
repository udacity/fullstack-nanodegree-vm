import psycopg2
from flask import Flask, request, session, g, redirect, url_for, \
     abort, render_template, flash

# Configure database
DATABASE = '/tmp/flaskr.db'
DEBUG = True
SECRET_KEY = 'development key'

USERNAME = 'admin'
PASSWORD = 'default'

# Configure flask
app = Flask(__name__)
app.config.from_object(__name__)

def connect():
    """Connect to the PostgreSQL database.  Returns a database connection."""
    return psycopg2.connect("dbname=catalog")


# Runs a query
def run_query(query):
    if type(query) is list:
        if len(query) >= 3:
            raise ValueError('Query can only contain up to 2 arguments')
    conn = connect()
    c = conn.cursor()
    if type(query) is str: # If query is just a string
        c.execute(query)
    else: # If it's an array, pass second param as data
        c.execute(query[0], query[1])
    ret = None
    try:
        ret = c.fetchall()
    except psycopg2.ProgrammingError:
        pass
    conn.commit()
    conn.close()
    return ret

@app.route("/")
def index():
    # return 'UPDATE items SET name=%s, category=%s, descrip=%s WHERE name=%s;' % ("Boots", "Skiis", "Skiing", "Skiis let you go down the hill!")
    return render_template('index.html', categories=get_categories(),  items=get_items())


@app.route("/catalog/<category>/items")
def category_items(category):
    items = run_query(["SELECT name, category FROM items WHERE category = %s;", (category, )])
    return render_template('category.html', all_categories=get_categories(), category=category, items=items, resno=len(items))


@app.route("/catalog/<category>/<item_name>")
def item_desc(category, item_name):
    item = run_query(["SELECT * FROM items WHERE category=%s AND name=%s;", (category, item_name)])[0]
    return render_template('item.html', item=item)


@app.route('/add-item', methods=['GET', 'POST'])
def add_item_page():
    if not session.get('logged_in'):
        abort(401)
    else:
        if request.method == 'POST':
            title = request.form['title']
            category = request.form['category']
            add_item(title, category, request.form['descrip'])
            return redirect('/catalog/' + category + '/' + title)
    return render_template('add-item.html', all_categories=get_categories(), action="/add-item", title="Add item", title_val="", desc_val="", cat_val="")


@app.route('/add-category', methods=['GET', 'POST'])
def add_category_page():
    if not session.get('logged_in'):
        abort(401)
    else:
        if request.method == 'POST':
            name = request.form['title']
            add_category(name)
            return redirect('/catalog/' + name + '/items')
    return render_template('add-category.html')


@app.route('/catalog/<item>/edit', methods=['GET', 'POST'])
def edit_item_page(item):
    action = '/catalog/' + item + '/edit'

    old_title = ""
    old_desc = ""
    old_cat = ""

    if not session.get('logged_in'):
        abort(401)
    else:
        query = run_query(["SELECT name, descrip, category FROM items WHERE name = %s;", (item, )])[0]
        old_title = query[0]
        old_desc = query[1]
        old_cat = query[2]
        if request.method == 'POST':
            new_title = request.form['title']
            new_category = request.form['category']
            edit_item(old_title, new_title, new_category, request.form['descrip'])
            return redirect('/catalog/' + new_category + '/' + new_title)

    return render_template('edit-item.html', all_categories=get_categories(), action=action, title="Edit item", title_val=old_title, desc_val=old_desc, cat_val=old_cat)


@app.route('/catalog/<item>/del-confirmation')
def delete_confirmation_page(item):
    return render_template('delete-item.html', item=item)


@app.route('/catalog/<item>/delete')
def delete_item_page(item):
    if not session.get('logged_in'):
        abort(401)
    else:
        delete_item(item)
    return redirect(url_for('index'))


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


@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    flash('You were logged out')
    return redirect(url_for('index'))


def add_category(category_name):
    run_query(["INSERT INTO categories(category) VALUES(%s);", (category_name, )])


def add_item(item_name, category, descrip):
    run_query(['INSERT INTO items(name, category, descrip) VALUES(%s, %s, %s);', (item_name, category, descrip)])


def edit_item(current_name, new_name, category, descrip):
    run_query(['UPDATE items SET name=%s, category=%s, descrip=%s WHERE name=%s;', (new_name, category, descrip, current_name)])


def delete_item(item_name):
    run_query(['DELETE FROM items WHERE name=%s;', (item_name,)])


def get_categories():
    return run_query("SELECT category FROM categories;")


def get_items():
    return run_query("SELECT name, category FROM items;")


def get_items_where(arg1, arg2):
    return run_query(["SELECT name, category FROM items WHERE %s = %s;", (arg1, arg2)])


if __name__ == "__main__":
    app.run(host='0.0.0.0')
