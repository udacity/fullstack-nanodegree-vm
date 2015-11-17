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

`http://localhost:8000/category/rss`
`http://localhost:8000/images/rss`
`http://localhost:8000/items/rss`

* **XML endpoints**

`http://localhost:8000/category/xml`
`http://localhost:8000/images/xml`
`http://localhost:8000/items/xml`

* **JSON endpoints**

`http://localhost:8000/category/json  `
`http://localhost:8000/images/json`
`http://localhost:8000/items/json`

Only Items, Categories, and Images are provided via endpoints, users information are not provided via endpoints.

**Security: Cross-Site Request Forgery (CSRF) Prevention.**
A new token is issued after each request.


### How to use this app:

**Clone the app.**

**go to vagrant/catalog:**
`Execute bash file: pg_config.sh`

**Execute the App with no data:**
`python app/create_catalog_no_items_db.py`
`python application.py`

Execute the App with data:
`python app/create_catalog_with_tems_db.py`
`python application.py`



