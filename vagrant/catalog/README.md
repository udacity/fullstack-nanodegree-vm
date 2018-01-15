# Setup Environment

run `vagrant ssh`

run `psql`

run `ALTER USER vagrant WITH PASSWORD 'vagrant'`;

run `cd /vagrant/catalog`

run `python setup_db.py`

run sudo pip install requests

run following commands:

```
sudo pip install werkzeug==0.8.3
sudo pip install flask==0.9
sudo pip install Flask-Login==0.1.3
```

Source: https://discussions.udacity.com/t/im-getting-the-not-json-serializable-when-i-used-the-login-code-provided-from-the-oauth/16010

# Run the application

## Start application

run `vagrant ssh`

run `cd /vagrant/catalog/`

run `python application.py`

## Run Application

open application in http://0.0.0.0:8000/
