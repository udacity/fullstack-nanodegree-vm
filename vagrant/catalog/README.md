# Welcome to *Catalog App*

**Catalog App** is an app repository where you can create your own catalog app. It is single page web application utilizing *AngularJS* along with *RequireJS* using the *Flask* framework with the *Python language*.

The app core is bootstrapped along with a core of structures.

The app allows you to view all items from previous users. However, you can only create or modify your own items.

The app allows you to login from either Google or Facebook. Multiple accounts with the same email behaves the same as your username account is your email.

The app also provides you with picture and images from our database of images.

You can access the app via: http://localhost:8000

## Technical Notes:

### The app supports all four operations:

* *Create*: Your can create your own items once you're logged in
* *Read*: You can read all items whether you're logged in or not
* *Update*: You can only update your own items once you're logged in
* *Delete*: Your can only delete your items once you're logged in

**Endpoints:**
The app provides several endpoints as:

* **RSS feeds using Atom feed library**

* `http://localhost:8000/category/rss`
* `http://localhost:8000/images/rss`
* `http://localhost:8000/items/rss`

* **XML endpoints**

* `http://localhost:8000/category/xml`
* `http://localhost:8000/images/xml`
* `http://localhost:8000/items/xml`

* **JSON endpoints**

* `http://localhost:8000/category/json `
* `http://localhost:8000/images/json`
* `http://localhost:8000/items/json`

Only Items, Categories, and Images are provided via endpoints, users information are not provided via endpoints.

**Security: Cross-Site Request Forgery (CSRF) Prevention.**
A new token is issued after each request.


### How to use this app:

**Clone the app.**

* Sprint up vagrant
	* 	*vagrant up*
* Log into the vagrant box
	* 	*vagrant ssh*
	* 	*cd /vagrant/catalog*

**Setup the environment:**

1. `pg_config.sh`
2. `sudo npm install bower -g`
3. `virtualenv app`
4. `. app/bin/activate`
5. `bower install --save`
> 	* You may need to select best version based on conflicts (always choose app).

**Likely you will need to install some pip app:**
`pip install flask==0.10.1 sqlalchemy requests werkzeug==0.10.4 watchdog==0.8.3 Flask-Login==0.1.3 httplib2 webapp2 webob oauth2client argparse`


**Execute the App with no data:**

1. `python application.py --clean`
2. `python application.py --with-no-data`
3. `python application.py`

**Execute the App with data:**

1. `python application.py --clean`
2. `python application.py --with-data`
3. `python application.py`



