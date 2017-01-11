from flask import Flask, render_template, url_for, request, redirect, flash, jsonify
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from setup_chisel_db import Base, Parks, Trails, User

#libraries for authentication
from flask import session as login_session
import random, string

# libraries for Oauth flow
from oauth2client.client import flow_from_clientsecrets
from oauth2client.client import FlowExchangeError
import httplib2
import json
from flask import make_response
import requests

# custom libraries
import routes

from modules import fboauth
from modules import goauth

app = Flask(__name__)


# Context processor for header.html to have access to logged-in user info
@app.context_processor
def inject_user():
    return dict(user=login_session)


@app.route('/parksJSON')
def parksJSON():
    return routes.parksJSON()

@app.route('/parks/<int:park_id>JSON')
def parkTrailsJSON(park_id):
    return routes.parkTrailsJSON(park_id)

@app.route('/trail/<int:trail_id>JSON')
def trailJSON(trail_id):
    return routes.trailJSON(trail_id)

# clear sessions for testing implementation
@app.route('/clearSession')
def clearSession():
    login_session.clear()
    flash('Session cleared')
    return redirect(url_for('parks'))

# Create anti-forgery state token
@app.route('/login')
def showLogin():
    state = ''.join(random.choice(string.ascii_uppercase + string.digits)
                    for x in xrange(32))
    login_session['state'] = state
    return render_template('login.html', state=state)

@app.route('/logout')
def logout():
    if login_session['account'] == 'Google':
        return redirect(url_for('gdisconnect'))
    else:
        return redirect(url_for('fbdisconnect'))

# FB Oauth flow
@app.route('/fbconnect', methods=['POST'])
def fbconnect():
    return fboauth.fbconnect()
@app.route('/fbdisconnect')
def fbdisconnect():
    return fboauth.fbdisconnect()

# Google Oauth flow
@app.route('/gconnect', methods=['POST'])
def gconnect():
    return goauth.gconnect()
@app.route("/gdisconnect")
def gdisconnect():
    return goauth.gdisconnect()

# Main Page, Parks
@app.route('/')
@app.route('/parks/', methods=['Get'])
def parks():
    return routes.parks()
@app.route('/search/', methods=['Get'])
def search():
    return routes.search()
@app.route('/parks/add', methods=['GET', 'POST'])
def addPark():
    return routes.addPark()
@app.route('/parks/<int:park_id>/delete/', methods=['GET', 'POST'])
def deletePark(park_id):
   return routes.deletePark(park_id)
@app.route('/parks/<int:park_id>/edit',
           methods=['GET', 'POST'])
def editPark(park_id):
   return routes.editPark(park_id)

# Park and Trail pages
@app.route('/parks/<int:park_id>/', methods=['Get'])
def park(park_id):
    return routes.park(park_id)
@app.route('/parks/<int:park_id>/add', methods=['GET', 'POST'])
def addTrail(park_id):
    return routes.addTrail(park_id)
@app.route('/parks/<int:park_id>/<int:trail_id>/edit',
           methods=['GET', 'POST'])
def editTrail(park_id, trail_id):
    return routes.editTrail(park_id, trail_id)
@app.route('/parks/<int:park_id>/<int:trail_id>/delete/', 
        methods=['GET', 'POST'])
def deleteTrail(park_id, trail_id):
    return routes.deleteTrail(park_id, trail_id)
@app.route('/parks/<int:park_id>/<int:trail_id>/')
def trail(park_id, trail_id):
    return routes.trail(park_id, trail_id)


if __name__ == '__main__':
    app.secret_key = 'super_secret_key'
    app.debug = True
    app.run(host='0.0.0.0', port=5000)