import json

CLIENT_ID = json.loads(open('app/client_secret.json',
                            'r').read())['web']['client_id']
APP_NAME = 'Catalop Web Application'
GOOGLE_AUTH = 'client_secret.json'
ERROR_401 = 'Unable to process information as requested'
# SQLALCHEMY_DATABASE_URI
APP_SECRET_KEY = 'Ev4gloAsQynGg0Puo3nlmY_r'
