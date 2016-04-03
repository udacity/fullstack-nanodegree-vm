import json

CLIENT_ID = json.loads(open('app/client_secrets.json',
                            'r').read())['web']['client_id']
APP_NAME = 'Catalop Web Application'
GOOGLE_AUTH = 'app/client_secrets.json'
ERROR_401 = 'Unable to process information as requested'
APP_SECRET_KEY = 'AIzaSyBnsw4CDFk8wyf06jZoSu18bzzt1Cct1SY'
FACEBOOK_KEY = ''
SQLALCHEMY_DATABASE_URI = 'postgresql://catalog:passDB@localhost/CatalogDb'

