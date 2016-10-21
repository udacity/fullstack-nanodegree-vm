from flask import Flask, render_template, url_for, request, \
        redirect, flash, jsonify
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from setup_chisel_db import Base, Parks, Trails, User

import cookies

# Connect to Database
engine = create_engine('sqlite:///chisel.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()


def search():
    parks = session.query(Parks).all()
    return render_template('search.html', parks=parks)

def parksJSON():
    parks = session.query(Parks).all()
    return jsonify(Restaurants=[p.serialize for p in parks])

def parkTrailsJSON(park_id):
    trails = session.query(Trails).filter_by(park_id=park_id).all()
    return jsonify(Trails=[t.serialize for t in trails])

def parks():
    parks = session.query(Parks).all()
    return render_template('parks.html', parks=parks)


def addPark():
    if request.method == 'POST':
        #Enforce Access
        uid_cookie = request.cookies.get('uid')
        if uid_cookie != '' and uid_cookie != None \
                and cookies.check_secure_val(uid_cookie):
            user_id = uid_cookie.split('|')[0]
            newPark = Parks(
                name=request.form['name'], lat=request.form['lat'], 
                lon=request.form['lon'], user_id=user_id)
            session.add(newPark)
            session.commit()
            #notify user
            flash('New park created')
            return redirect(url_for('parks'))
        else:
            flash('Must be logged in to add a park')
            return redirect(url_for('parks'))
    #Get
    else:
        return render_template('addPark.html')


def deletePark(park_id):
    park = session.query(Parks).filter_by(id=park_id).one()
    if request.method == 'POST':
        #Enforce Access
        uid_cookie = request.cookies.get('uid')
        if uid_cookie != '' and uid_cookie != None \
                and cookies.check_secure_val(uid_cookie):
            #Enforce Authorization
            if uid_cookie.split('|')[0] == str(park.user_id):
                session.delete(park)
                session.commit()
                #notify user
                flash('%s deleted' % park.name)
                return redirect(url_for('parks'))
            else:
                flash('You must be the author of this park to delete it' )
                return redirect(url_for('park', park_id=park_id))
        else:
            flash('Must be logged in to delete a park')
            return redirect(url_for('park', park_id=park_id))
    #Get
    else:
        return render_template('deletePark.html', park=park)


def editPark(park_id):
    park = session.query(Parks).filter_by(id=park_id).one()
    if request.method == 'POST':
        #Enforce Access
        uid_cookie = request.cookies.get('uid')
        if uid_cookie != '' and uid_cookie != None \
                and cookies.check_secure_val(uid_cookie):
            #Enforce Authorization
            if uid_cookie.split('|')[0] == str(park.user_id):
                if request.form['name']:
                    park.name = request.form['name']
                    park.lon = request.form['lon']
                    park.lat = request.form['lat']
                session.add(park)
                session.commit()
                #notify user
                flash('%s edited' % park.name)
                return redirect(url_for('parks'))
            else:
                flash('You must be the author of this park to delete it')
                return redirect(url_for('park', park_id=park_id))
        else:
            flash('Must be logged in to edit a park')
            return redirect(url_for('park', park_id=park_id))
    #Get
    else:
        return render_template('editPark.html', park=park)


def park(park_id):
    park = session.query(Parks).filter_by(id=park_id).one()
    trails = session.query(Trails).filter_by(park_id=park_id)
    return render_template('park.html', trails=trails, park=park)

def trail(park_id, trail_id):
    park = session.query(Parks).filter_by(id=park_id).one()
    trail = session.query(Trails).filter_by(id=trail_id).one()
    return render_template('trail.html', trail=trail, park=park)

def addTrail(park_id):
    if request.method == 'POST':
        uid_cookie = request.cookies.get('uid')
        # Enforce Access
        if uid_cookie != '' and uid_cookie != None \
                and cookies.check_secure_val(uid_cookie):
            user_id = uid_cookie.split('|')[0]
            newTrail = Trails(name=request.form['name'],
                            park_id=park_id, user_id=user_id)
            session.add(newTrail)
            session.commit()
            #notify user
            flash('New trail created')
            return redirect(url_for('park', park_id=park_id))
        else:
            flash('Must be logged in to add a new trail')
            return redirect(url_for('park', park_id=park_id))
    else:
        return render_template('addTrail.html', park_id=park_id)


def editTrail(park_id, trail_id):
    trail = session.query(Trails).filter_by(id=trail_id).one()
    if request.method == 'POST':
        uid_cookie = request.cookies.get('uid')
        # Enforce Access
        if uid_cookie != '' and uid_cookie != None \
                and cookies.check_secure_val(uid_cookie):
            #Enforce Authorization
            if uid_cookie.split('|')[0] == str(trail.user_id):
                name = request.form['name']
                if name:
                    trail.name = name
                session.add(trail)
                session.commit()
                #notify user
                flash('%s edited' % trail.name)
                return redirect(url_for('park', park_id=park_id))
            else:
                flash('You must be the author of this trail to edit it')
                return redirect(
                        url_for('trail', park_id=park_id, trail_id=trail_id))
        else:
            flash('Must be logged in to edit a trail')
            return redirect(url_for('park', park_id=park_id))
        
    else:
        # USE THE RENDER_TEMPLATE FUNCTION BELOW TO SEE THE VARIABLES YOU
        # SHOULD USE IN YOUR EDITMENUITEM TEMPLATE
        return render_template(
            'editTrail.html', park_id=park_id,
            trail_id=trail_id, trail=trail)


def deleteTrail(park_id, trail_id):
    trail = session.query(Trails).filter_by(id=trail_id).one()
    if request.method == 'POST':
        #Enforce Access
        uid_cookie = request.cookies.get('uid')
        if uid_cookie != '' and uid_cookie != None \
                and cookies.check_secure_val(uid_cookie):
            #Enforce Authorization
            if uid_cookie.split('|')[0] == str(trail.user_id):
                session.delete(trail)
                session.commit()
                #notify user
                flash('%s deleted' % trail.name)
                return redirect(url_for('park', park_id=park_id))
            else:
                flash('You must be the author of this trial to delete it')
                return redirect(
                        url_for('trail', park_id=park_id, trail_id=trail_id))
        else:
            flash('Must be logged in to delete content')
            return redirect( url_for('parks'))
    else:
        return render_template('deleteTrail.html', park_id=park_id, trail=trail)