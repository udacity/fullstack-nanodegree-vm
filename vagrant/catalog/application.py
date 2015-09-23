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
    return render_template('index.html', categories=get_categories(),  items=get_items())


@app.route("/catalog/<category>/items")
def category_items(category):
    items = run_query(["SELECT name, category FROM items WHERE category = %s;", (category, )])
    return render_template('category.html', all_categories=get_categories(), category=category, items=items, resno=len(items))


@app.route("/catalog/<category>/<item_name>")
def item_desc(category, item_name):
    item = run_query(["SELECT name, category, descrip FROM items WHERE category=%s AND name=%s;", (category, item_name)])[0]
    return render_template('item.html', item=item)


@app.route('/add', methods=['GET', 'POST'])
def add_item_page():
    if not session.get('logged_in'):
        abort(401)
    else:
        if request.method == 'POST':
            add_item(request.form['title'], request.form['category'], request.form['descrip'])
            return redirect(url_for('index'))
    return render_template('add.html', all_categories=get_categories())


@app.route('/edit', methods=['GET', 'POST'])
def edit_item_page():
    if not session.get('logged_in'):
        abort(401)
    return render_template('edit.html', all_categories=get_categories())

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


def get_categories():
    return run_query("SELECT category FROM categories;")


def get_items():
    return run_query("SELECT name, category FROM items;")


def get_items_where(arg1, arg2):
    return run_query(["SELECT name, category FROM items WHERE %s = %s;", (arg1, arg2)])

if __name__ == "__main__":
    app.run(host='0.0.0.0')
