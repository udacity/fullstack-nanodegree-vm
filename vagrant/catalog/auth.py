from flask_oauth import OAuth

# https://pythonhosted.org/Flask-OAuth/
'''
Based off of:
https://github.com/mitsuhiko/flask-oauth/blob/master/example/google.py
'''

GOOGLE_CLIENT_ID = '517196448068-sv03nb9nf9gs0clm7pkt3i269nu4ctdp.apps.googleusercontent.com'
GOOGLE_CLIENT_SECRET = 'L_dSVaUvOazuNrDrh2FPyp85'
REDIRECT_URI = '/authorized'

oauth = OAuth()

google = oauth.remote_app(
    'google',
    base_url='https://www.google.com/accounts/',
    authorize_url='https://accounts.google.com/o/oauth2/auth',
    request_token_url=None,
    request_token_params={'scope': 'https://www.googleapis.com/auth/userinfo.email',
                        'response_type': 'code'},
    access_token_url='https://accounts.google.com/o/oauth2/token',
    access_token_method='POST',
    access_token_params={'grant_type': 'authorization_code'},
    consumer_key=GOOGLE_CLIENT_ID,
    consumer_secret=GOOGLE_CLIENT_SECRET
)