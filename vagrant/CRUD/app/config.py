import os
CSRF_ENABLED = True
DEBUG = True
SERVER = 'http://localhost:8000'
TRAP_BAD_REQUEST_ERRORS = True
TRAP_HTTP_EXCEPTIONS = True
SQLALCHEMY_ECHO = True
SQLALCHEMY_DATABASE_URI = 'mysql+mysqldb://quantel@tongariro-i7/jira_customers?charset=utf8'  # noqa

# Generate a random secret key
SECRET_KEY = "SpankyPants"
basedir = os.path.abspath(os.path.dirname(__file__))
WHOOSH_BASE = os.path.join(basedir, 'search.db')
