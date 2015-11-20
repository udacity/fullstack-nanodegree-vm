WTF_CSRF_ENABLED = True
SECRET_KEY = 'you-will-never-guess'
DEBUG = True
SQLALCHEMY_DATABASE_URI = 'mysql+mysqldb://quantel@tongariro-i7/jira_customers_test?charset=utf8'  # noqa
SERVER = 'http://localhost:8000'
TRAP_BAD_REQUEST_ERRORS = True
TRAP_HTTP_EXCEPTIONS = True

OPENID_PROVIDERS = [
    {'name': 'Google', 'url': 'https://www.google.com/accounts/o8/id'},
    {'name': 'Yahoo', 'url': 'https://me.yahoo.com'},
    {'name': 'AOL', 'url': 'http://openid.aol.com/<username>'},
    {'name': 'Flickr', 'url': 'http://www.flickr.com/<username>'},
    {'name': 'MyOpenID', 'url': 'https://www.myopenid.com'}]
