from flask import Flask, render_template, url_for, redirect, request, flash, jsonify
app = Flask(__name__)

from sqlalchemy import create_engine, desc
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Game, UsersGames, User

from flask import session as login_session
import random, string
from datetime import datetime

from oauth2client.client import flow_from_clientsecrets
from oauth2client.client import FlowExchangeError
import httplib2
import json
from flask import make_response
import requests

CLIENT_ID = json.loads(
    open('client_secrets.json', 'r').read())['web']['client_id']
APPLICATION_NAME = "Gamerater"

# Create database
engine = create_engine('sqlite:///favoritegames.db')
Base.metadata.create_all(engine)

# Create database connector
DBSession = sessionmaker(bind = engine)
session = DBSession()

# Methods used
methods = ['GET', 'POST']

# Helper functions
def get_user_by_id(user_id):
    """Function for getting a user object given the user id."""
    return session.query(User).filter_by(id = user_id).one()

def get_user_id_by_email(email):
    """
    Function for getting the user id for the given email. If the user
    id cannot be found, returns None.
    """
    try:
        user = session.query(User).filter_by(email = email).one()
        return user.id
    except:
        return None

def get_game_by_id(game_id):
    """Returns a game object with the given game_id."""
    return session.query(Game).filter_by(id = game_id).one()

def get_game_by_name(game_name):
    """Returns a game object with the given game_id."""
    return session.query(Game).filter_by(name = game_name).one()

def get_ratings_by_game_id(game_id):
    """Returns the ratings with the given game_id."""
    return session.query(UsersGames).filter_by(game_id = game_id).all()

def get_ratings_by_user_id(user_id):
    """Returns the ratings for user with the given id."""
    return session.query(UsersGames).filter_by(
        user_id = user_id).order_by(desc(UsersGames.rating)).all()

def get_rating_by_user_and_game(user_id, game_id):
    """Returns the rating with the given user_id and game_id."""
    return session.query(UsersGames).filter(
        UsersGames.user_id == user_id, UsersGames.game_id == game_id).one()

def get_top_game_by_user_id(user_id):
    """
    Returns the game with the highest rating by the user with
    id user_id.
    """
    top_rating = session.query(UsersGames).filter_by(
        user_id = user_id).order_by(desc(UsersGames.rating)).limit(1).one()
    return get_game_by_id(top_rating.game_id)

def get_latest_game_by_user_id(user_id):
    """Returns the game most recently rated by the given user_id."""
    latest_rating = session.query(UsersGames).filter_by(
        user_id = user_id).order_by(desc(UsersGames.modified)).limit(1).one()
    return get_game_by_id(latest_rating.game_id)

def update_game_avg_rating(game_id):
    """Refreshes the average rating for game_id."""

    # Get the existing game ratings, then divide by num ratings
    existing_ratings = session.query(UsersGames).filter_by(
        game_id = existing_game.id)
    ratings_count = existing_ratings.count()
    all_ratings = []
    for rating in existing_ratings.all():
        all_ratings.append(rating.rating)
    avg_rating = float(sum(all_ratings)) / ratings_count
    existing_game.avg_rating = avg_rating
    existing_game.modified = datetime.now()
    session.add(existing_game)
    session.commit()


def make_json_response(message, code):
    """
    Returns a json response with the given message and code.

    response = make_json_response("Invalid state", 401)
    """
    response = make_response(json.dumps(message), code)
    response.headers['Content-Type'] = 'application/json'
    return response

def create_user(login_session):
    new_user = User(name=login_session['username'],
                    email=login_session['email'],
                    picture=login_session['picture'])
    session.add(new_user)
    session.commit()
    return new_user

def login_or_create_user(login_session):
    """See if user exists, and create the user if not."""
    user_id = get_user_id_by_email(login_session['email'])
    if not user_id:
        user = create_user(login_session)
    else:
        user = get_user_by_id(user_id)

    login_session['user_id'] = user.id

    if user.name:
        login_session['username'] = user.name


    output = ''
    output += '<h1>Welcome, '
    output += login_session['username']
    output += '!</h1>'
    output += '<img src="'
    output += login_session['picture']
    output += (' " style = "width: 300px; height: 300px;border-radius: '
               '150px;-webkit-border-radius: 150px;-moz-border-radius: '
               '150px;"> ')
    return output


# Route handling functions
@app.route('/gconnect', methods=['POST'])
def gconnect():
    """Logs the user in using Google third party authentication."""

    if request.args.get('state') != login_session['state']:
        return make_json_response('Invalid state parameter', 401)
    code = request.data

    try:
        # Upgrade the authorization code into a credentials object
        oauth_flow = flow_from_clientsecrets('client_secrets.json', scope='')
        oauth_flow.redirect_uri = 'postmessage'
        credentials = oauth_flow.step2_exchange(code)
    except FlowExchangeError:
        return make_json_response(
            'Failed to upgrade the authorization code', 401)

    # Check that the access token is valid
    access_token = credentials.access_token
    url = ('https://www.googleapis.com/oauth2/v1/tokeninfo?access_token=%s' % (
        access_token))
    h = httplib2.Http()
    result = json.loads(h.request(url, 'GET')[1])

    # If there was an error in the access token info, abort.
    if result.get('error') is not None:
        return make_json_response(result.get('error'), 500)

    # Verify that the access token is used for the intended user.
    gplus_id = credentials.id_token['sub']
    if result['user_id'] != gplus_id:
        message = "Token's user ID doesn't match given user ID."
        return make_json_response(message, 401)

    # Verify that the access token is valid for this app
    if result['issued_to'] != CLIENT_ID:
        message = "Token's client ID does not match app's."
        print message
        return make_json_response(message, 401)

    # Check to see if user is already logged in
    stored_credentials = login_session.get('credentials')
    stored_gplus_id = login_session.get('gplus_id')
    if stored_credentials is not None and gplus_id == stored_gplus_id:
        return make_json_response('Current user is already connected.', 200)

    # Store the access token in the session for later use.
    login_session['credentials'] = credentials
    login_session['gplus_id'] = gplus_id

    # Get user info
    userinfo_url = "https://www.googleapis.com/oauth2/v1/userinfo"
    params = {'access_token': credentials.access_token, 'alt' : 'json'}
    answer = requests.get(userinfo_url, params=params)
    data = json.loads(answer.text)

    login_session['username'] = data['name']
    login_session['picture'] = data['picture']
    login_session['email'] = data['email']
    login_session['provider'] = 'google'

    # See if user exists, and create the user if not.
    output = login_or_create_user(login_session)
    flash("You are now logged in as %s" % login_session['username'])
    print "done!"
    return output

@app.route("/gdisconnect")
def gdisconnect():
    """
    Disconnects a logged in user. Should only be used with
    a connected user.
    """
    credentials = login_session.get('credentials')
    if credentials is None:
        return make_json_response("Current user not connected.", 401)

    # Execute HTTP GET request to revoke current token.
    access_token = credentials.access_token
    url = ('https://accounts.google.com/o/oauth2/revoke?token=%s' % (
        access_token))
    h = httplib2.Http()
    result = h.request(url, 'GET')[0]

    if result['status'] == '200':
        return make_json_response('Successfully disconnected.', 200)
    else:
        # For whatever reason, the given token was invalid.
        return make_json_response(
            'Failed to revoke token for given user.', 400)

@app.route('/fbconnect', methods=['POST'])
def fbconnect():
    if request.args.get('state') != login_session['state']:
        return make_json_response('Invalid sate parameter', 401)
    access_token = request.data

    # Exchange client token for long-lived server-side token with GET
    # /oauth/access_token?grant_type=fb_exchange_token&client_id=
    # {app-id}&client_secret={app-secret}&fb_exchange_token=
    # {short-lived-token}
    app_id = json.loads(
        open('fb_client_secrets.json', 'r').read())['web']['app_id']
    app_secret = json.loads(
        open('fb_client_secrets.json', 'r').read())['web']['app_secret']
    url = ('https://graph.facebook.com/oauth/access_token?grant_type=fb_exchange_token&client_id='
           '%s&client_secret=%s&fb_exchange_token=%s' % (
            app_id, app_secret, access_token))
    h = httplib2.Http()
    result = h.request(url, 'GET')[1]

    # Use token to user info from API
    userinfo_url = "https://graph.facebook.com/v2.4/me"
    # Strip expire tag from access token
    token = result.split("&")[0]

    url = 'https://graph.facebook.com/v2.4/me?%s&fields=name,id,email' % token
    h = httplib2.Http()
    result = h.request(url, 'GET')[1]
    #print "url sent for API access: %s" % url
    #print "API JSON result: %s" % result
    data = json.loads(result)
    login_session['provider'] = 'facebook'
    login_session['username'] = data["name"]
    login_session['email'] = data["email"]
    login_session['facebook_id'] = data["id"]
    login_session['provider'] = 'facebook'

    # Get user picture
    url = ('https://graph.facebook.com/v2.4/me/picture?%s&redirect=0'
           '&height=100&width=100' % token)
    h = httplib2.Http()
    result = h.request(url, 'GET')[1]
    data = json.loads(result)

    login_session['picture'] = data['data']['url']

    # See if user exists, and create the user if not.
    output = login_or_create_user(login_session)
    flash("You are now logged in as %s" % login_session['username'])
    print "done!"
    return output

@app.route('/fbdisconnect/')
def fbdisconnect():
    facebook_id = login_session['facebook_id']
    url = 'https://graph.facebook.com/%s/permissions' % facebook_id
    h = httplib2.Http()
    result = h.request(url, 'DELETE')[1]

@app.route('/disconnect/')
def disconnect():
    if 'provider' in login_session:
        if login_session['provider'] == 'google':
            gdisconnect()
            del login_session['gplus_id']
            del login_session['credentials']
        if login_session['provider'] == 'facebook':
            fbdisconnect()
            del login_session['facebook_id']

        del login_session['username']
        del login_session['email']
        del login_session['picture']
        del login_session['user_id']
        del login_session['provider']
        flash("You have successfully been logged out.")
        return redirect(url_for('gamerater_home'))
    else:
        flash("You were not logged in to begin with!")
        redirect(url_for('gamerater_home'))

@app.route('/login/')
def show_login():
    state = ''.join(random.choice(
        string.ascii_uppercase + string.digits) for x in xrange(32))
    login_session['state'] = state
    return render_template('login.html', STATE=state)

@app.route('/update_user', methods = methods)
def update_user():
    # If the user isn't logged in, redirect to login
    if not login_session:
        return redirect(url_for('show_login'))

    if request.method == 'POST':

        # If the user submitted cancel, redirect home
        if request.form['submit'] == 'Cancel':
            return redirect(url_for('gamerater_home'))

        # Get the user's entry
        username = request.form['username']

        # Check if username and email both were submitted
        if not username:
            flash("Please enter a username.")
            return render_template(
                'update_user.html', username = username)

        # Get the user and update
        user = session.query(User).filter_by(
            id = login_session['user_id']).one()

        print "adding username to session"
        user.name = username
        session.add(user)
        session.commit()

        login_session['username'] = username

        return redirect(url_for('my_games'))

    return render_template(
        'update_user.html', username = login_session['username'])

@app.route('/')
@app.route('/gamerater/')
def gamerater_home():
    # Get the 10 most recent games
    recent_ten_ratings = session.query(UsersGames).order_by(
        desc(UsersGames.modified)).limit(10)
    recent_games = []
    for rating in recent_ten_ratings:
        recent_game = {
            "user" : get_user_by_id(rating.user_id),
            "game" : get_game_by_id(rating.game_id),
            "rating" : rating.rating,
            "modified" : rating.modified
        }
        recent_games.append(recent_game)

    # Get the 10 highest ratings
    top_ten_games = session.query(Game).order_by(
        desc(Game.avg_rating)).limit(10)

    # Get all users
    all_users = session.query(User).all()

    users = []

    for user in all_users:
        try:
            favorite_game = get_top_game_by_user_id(user.id).name
            latest_game = get_latest_game_by_user_id(user.id).name
        except:
            favorite_game = "This user does not have a rating yet."
            latest_game = "This user does not have a rating yet."

        user_data = {
            'user' : user,
            'favorite_game' : favorite_game,
            'latest_game' : latest_game
        }
        users.append(user_data)

    return render_template("home.html",
                           recent_games = recent_games,
                           top_ten_games = top_ten_games,
                           users = users)

@app.route('/gamerater/game/<int:game_id>/')
def game_info(game_id):
    # Try getting the game info. If an exception occurs, return error
    try:
        game = get_game_by_id(game_id)
    except:
        flash("We're sorry, that's not a valid game id!")
        return redirect(url_for('gamerater_home'))
    
    # Get the ratings info
    rating_data = get_ratings_by_game_id(game_id=game_id)
    
    # Set up data for the page
    ratings = []
    for rating in rating_data:
        user_rating = {
            "user" : get_user_by_id(rating.user_id),
            "user_id" : rating.user_id,
            "rating" : rating.rating
        }
        ratings.append(user_rating)
    return render_template("game.html", game = game, ratings = ratings)

@app.route('/gamerater/user/<int:user_id>/')
def user_info(user_id):
    # Get the user info
    try:
        user = get_user_by_id(user_id)
    except:
        flash("We're sorry, that user id does not exist.")
        return redirect(url_for('gamerater_home'))

    # Get the user's ratings
    try:
        users_ratings = get_ratings_by_user_id(user.id)
    except:
        users_ratings = None

    # Setup the ratings for the page
    if users_ratings:
        ratings = []
        for rating in users_ratings:
            new_rating = {
                'rating' : rating.rating,
                'game' : get_game_by_id(rating.game_id)
            }
            ratings.append(new_rating)
    else:
        ratings = None

    # Get the user's top rating
    try:
        game = get_top_game_by_user_id(user_id=user_id)
    except:
        game = None

    return render_template("user.html",
                           user = user,
                           ratings = ratings,
                           game = game)

@app.route('/gamerater/add-game', methods = methods)
def add_game():
    # Require the user to be logged in
    if 'username' not in login_session:
            return redirect('/login')

    if request.method == 'POST':

        # Redirect home if you press Cancel
        if request.form['submit'] == 'Cancel':
            return redirect(url_for('gamerater_home'))

        game_name = request.form['name']
        category = request.form['category']
        description = request.form['description']
        rating = request.form['rating']
        
        # Double check if the game actually exists
        try:
            existing_game = get_game_by_name(game_name=game_name)
            flash("That game already exists! Please add a rating.")
            return redirect(url_for('rate_game',
                                    game_name = game_name,
                                    rating = rating))
        except:
            # If any fields are missing return an error
            if not (game_name and category and description):
                flash('Please enter text in each field.')
                return render_template('add_game.html',
                                       game_name = game_name,
                                       category = category,
                                       description = description,
                                       rating = rating)

            # If the rating is not an integer between 0 and 10 return
            # an error
            try:
                rating_int = int(rating)
                if rating_int > 10 or rating_int < 0:
                    flash('Please ensure the rating is a number from 1 to 10.')
                    return render_template('rate_game.html',
                                           game_name = game_name,
                                           rating = rating)
            except:
                flash('Please ensure the rating is a number from 1 to 10.')
                return render_template('rate_game.html',
                                        game_name = game_name,
                                        rating = rating)
            
            # Add new game and new rating
            new_game = Game(name = game_name,
                            category=category,
                            description=description,
                            avg_rating=rating_int,
                            modified=datetime.now())
            session.add(new_game)
            session.commit()
            game_to_rate = get_game_by_name(game_name=game_name)
            new_rating = UsersGames(user_id = login_session['user_id'],
                                    game_id = game_to_rate.id,
                                    rating = rating_int,
                                    modified = datetime.now())
            session.add(new_rating)
            session.commit()
            flash('%s has been rated!' % game_to_rate.name)
            return redirect(url_for('my_games'))
    else:
        game_name = request.args.get('game_name')
        rating = request.args.get('rating')
        if not game_name:
            game_name = ""
        if not rating:
            rating = ""
        return render_template("add_game.html",
                               game_name = game_name,
                               rating = rating)

@app.route('/gamerater/rate-game', methods=methods)
def rate_game():
    # Require the user to be logged in
    if 'username' not in login_session:
            return redirect('/login')

    if request.method == 'POST':
        if request.form['submit'] == 'Cancel':
            return redirect('/')

        # Get post data
        game_name = request.form['name']
        rating = request.form['rating']

        # If either were not sent return an error
        if not (game_name and rating):
            flash('Please enter both a game name and rating.')
            return render_template('rate_game.html',
                                   game_name = game_name,
                                   rating = rating)

        # If the rating is not an integer between 0 and 10 return
        # an error
        try:
            rating_int = int(rating)
            if rating_int > 10 or rating_int < 0:
                flash('Please ensure the rating is a number from 1 to 10.')
                return render_template('rate_game.html',
                                       game_name = game_name,
                                       rating = rating)
        except:
            flash('Please ensure the rating is a number from 1 to 10.')
            return render_template('rate_game.html',
                                   game_name = game_name,
                                   rating = rating)

        # Try getting the existing game. If it doesn't exist,
        # redirect the user to add_game
        try:
            existing_game = get_game_by_name(game_name=game_name)
        except:
            return redirect(url_for('add_game',
                                    game_name = game_name,
                                    rating = rating))

        # Check if there's an existing rating. Update if so.
        try:
            existing_rating = get_rating_by_user_and_game(
                user_id = login_session['user_id'],
                game_id = existing_game.id)
            existing_rating.rating = rating_int
            session.add(existing_rating)
            session.commit()
            flash("The rating for %s has been updated with %s!" % (
                existing_game.name, existing_rating.rating))
        except:
            # Create a new rating if there isn't an existing one
            new_rating = UsersGames(user_id = login_session['user_id'],
                                    game_id = existing_game.id,
                                    rating = rating_int,
                                    modified = datetime.now())
            session.add(new_rating)
            session.commit()
            flash("%s has been rated." % existing_game.name)

        # Update the game's average rating
        update_game_avg_rating(game_id=game_id)

        return redirect(url_for('my_games'))

    
    game_name = request.args.get('game_name')
    rating = request.args.get('rating')
    if not game_name:
        game_name = ""
    if not rating:
        rating = ""
    return render_template("rate_game.html",
                           game_name = game_name,
                           rating = rating)

@app.route('/gamerater/delete_rating/<int:game_id>/', methods=methods)
def delete_rating(game_id):
    # If the user isn't logged in redirect to login
    if 'username' not in login_session:
            return redirect(url_for('show_login'))

    # Get the game for the rating
    # Redirect to add game if it doesn't exist
    try:
        game = get_game_by_id(game_id)
    except:
        flash("Sorry, we don't have a game with that id. "
              "Would you like to add a game?")
        return redirect(url_for('add_game'))

    # Get the rating. Redirect to rate game if it doesn't exist
    try:
        rating_to_delete = get_rating_by_user_and_game(
            user_id = login_session['user_id'],
            game_id = game.id)
    except:
        flash("Sorry, it looks like you haven't rated that game yet."
              "Would you like to?")
        return redirect(url_for('rate_game'))

    if request.method == 'POST':
        if "No" in request.form['submit']:
            print "No was in submit \n"
            return redirect(url_for('my_games'))

        # Delete the rating
        session.delete(rating_to_delete)
        session.commit()

        # Update the game's average rating
        update_game_avg_rating(game_id=game.id)
        
        flash("Your rating for %s has been deleted." % game.name)
        return redirect(url_for('my_games'))

    return render_template('delete_rating.html', game = game)

@app.route('/gamerater/my-games')
def my_games():
    # If the user isn't logged in redirect to login
    if 'username' not in login_session:
            return redirect(url_for('show_login'))

    if not login_session['username']:
        return redirect(url_for('update_user'))

    user_id = login_session['user_id']
    user = get_user_by_id(user_id)

    # Get the user's ratings
    try:
        users_ratings = get_ratings_by_user_id(user_id)
    except:
        users_ratings = None

    # Setup the ratings for the page
    if users_ratings:
        ratings = []
        for rating in users_ratings:
            new_rating = {
                'rating' : rating.rating,
                'game' : get_game_by_id(rating.game_id)
            }
            ratings.append(new_rating)
    else:
        ratings = None

    # Get the user's top rating
    try:
        top_rating = session.query(UsersGames).filter_by(
            user_id=user_id).order_by(desc(UsersGames.rating)).limit(1).one()
        game = get_game_by_id(top_rating.game_id)
    except:
        game = None

    return render_template("my_games.html",
                           user = user,
                           ratings = ratings,
                           game = game)

if __name__ == '__main__':
    app.secret_key = 'super_secret_key'
    app.debug = True
    app.run(host = '0.0.0.0', port = 8000)