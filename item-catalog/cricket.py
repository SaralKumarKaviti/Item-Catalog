from flask import Flask, render_template, request
from flask import redirect, url_for, jsonify, flash
from sqlalchemy import create_engine, asc
from sqlalchemy.orm import sessionmaker
from cricket_database import Country, Base, Player, User
from flask import session as login_session
import random
import string
import json

from oauth2client.client import flow_from_clientsecrets
from oauth2client.client import FlowExchangeError
import httplib2
from flask import make_response
import requests

app = Flask(__name__)

CLIENT_ID = json.loads(
    open('client_secrets.json', 'r').read())['web']['client_id']
APPLICATION_NAME = "Cricket Player item-catalog"
engine = create_engine(
    'sqlite:///cricketplayer.db', connect_args={'check_same_thread': False},
    echo=True)
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()


# For User login
@app.route('/login')
def showLogin():
    state = ''.join(random.choice(string.ascii_uppercase + string.digits)
                    for x in xrange(32))
    login_session['state'] = state
    # return "The current state is %s" %login_session['state']
    country = session.query(Country).all()
    player = session.query(Player).all()
    return render_template('login.html', STATE=state, country=country,
                           player=player)


# If User already logged
@app.route('/gconnect', methods=['POST'])
def gconnect():
    if request.args.get('state') != login_session['state']:
        response = make_response(json.dumps('Invalid State parameter'), 401)
        response.headers['Content-Type'] = 'application/json'
        return response
    code = request.data

    try:
        oauth_flow = flow_from_clientsecrets('client_secrets.json', scope='')
        oauth_flow.redirect_uri = 'postmessage'
        credentials = oauth_flow.step2_exchange(code)
    except FlowExchangeError:
        response = make_response(
            json.dumps('Failed to upgrade the authorization code.'), 401)
        response.headers['Content-Type'] = 'application/json'
        return response

    access_token = credentials.access_token
    url = ('https://www.googleapis.com/oauth2/v1/tokeninfo?access_token=%s'
           % access_token)
    h = httplib2.Http()
    result = json.loads(h.request(url, 'GET')[1])

    if result.get('error') is not None:
        response = make_response(json.dumps(result.get('error')), 500)
        response.headers['Content-Type'] = 'application/json'
        return response

    gplus_id = credentials.id_token['sub']
    if result['user_id'] != gplus_id:
        response = make_response(
            json.dumps("Token's user ID doesn't match given user ID."), 401)
        response.headers['Content-Type'] = 'application/json'
        return response

    if result['issued_to'] != CLIENT_ID:
        response = make_response(
            json.dumps("Token's client ID does not match app's."), 401)
        print("Token's client ID does not match app's.")
        response.headers['Content-Type'] = 'application/json'
        return response

    stored_access_token = login_session.get('access_token')
    stored_gplus_id = login_session.get('gplus_id')
    if stored_access_token is not None and gplus_id == stored_gplus_id:
        response = make_response(
                                 json.dumps(
                                            'Current user already connected'),
                                 200)
        response.headers['Content-Type'] = 'application/json'
        return response

    login_session['access_token'] = credentials.access_token
    login_session['gplus_id'] = gplus_id

    userinfo_url = "https://www.googleapis.com/oauth2/v1/userinfo"
    params = {'access_token': credentials.access_token, 'alt': 'json'}
    answer = requests.get(userinfo_url, params=params)

    data = answer.json()

    login_session['username'] = data['name']
    login_session['picture'] = data['picture']
    login_session['email'] = data['email']

    user_id = getUserID(login_session['email'])
    if not user_id:
        user_id = createUser(login_session)
    login_session['user_id'] = user_id

    output = ''
    output += '<center><h2><font color="green">Welcome '
    output += login_session['username']
    output += '!</font></h2></center>'
    output += '<center><img src="'
    output += login_session['picture']
    output += ' " style = "width: 200px; -webkit-border-radius: 200px;" '
    output += ' " style = "height: 200px;border-radius: 200px;" '
    output += ' " style = "-moz-border-radius: 200px;"></center>" '
    flash("you are now logged in as %s" % login_session['username'])
    print("Done")
    return output


# Create New User
def createUser(login_session):
    newUser = User(name=login_session['username'],
                   email=login_session['email'],
                   picture=login_session['picture'])
    session.add(newUser)
    session.commit()

    user = session.query(User).filter_by(email=login_session['email']).one()
    return user.id


# Getting information of user
def getUserInfo(user_id):
    user = session.query(User).filter_by(id=user_id).one()
    return user


# Getting user email address
def getUserID(email):
    try:
        user = session.query(User).filter_by(email=email).one()
        return user.id
    except Exception as e:
        return None


# To read country JSON data on web browser
@app.route('/country/JSON')
def countryJSON():
    country = session.query(Country).all()
    return jsonify(country=[c.serialize for c in country])


# To read country wise of player JSON
@app.route('/country/<int:country_id>/menu/<int:player_id>/JSON')
def countryListJSON(country_id, player_id):
    Player_List = session.query(Player).filter_by(id=player_id).one()
    return jsonify(Player_List=Player_List.serialize)


# To read players JSON
@app.route('/country/<int:player_id>/menu/JSON')
def playerListJSON(player_id):
    country = session.query(Country).filter_by(id=player_id).one()
    player = session.query(Player).filter_by(player_id=country.id).all()
    return jsonify(PlayerLists=[i.serialize for i in player])


# This is a home page of entire project
@app.route('/country/')
def showCountry():
    country = session.query(Country).all()
    return render_template('country.html', country=country)


# Create new Country
@app.route('/country/new/', methods=['GET', 'POST'])
def newCountry():
    if 'username' not in login_session:
        return redirect('/login')
    if request.method == 'POST':
        newCountry = Country(name=request.form['name'],
                             user_id=login_session['user_id'])
        session.add(newCountry)
        session.commit()
        return redirect(url_for('showCountry'))
    else:
        return render_template('newCountry.html')


# To Editing existing country name
@app.route('/country/<int:country_id>/edit/', methods=['GET', 'POST'])
def editCountry(country_id):
    if 'username' not in login_session:
        return redirect('/login')
    editedCountry = session.query(Country).filter_by(id=country_id).one()
    creater_id = getUserInfo(editedCountry.user_id)
    user_id = getUserInfo(login_session['user_id'])
    if creater_id.id != login_session['user_id']:
        flash("You cannot edit this Country "
              "This is belongs to %s" % (creater_id.name))
        return redirect(url_for('showCountry'))
    if request.method == 'POST':
        if request.form['name']:
            editedCountry.name = request.form['name']
            flash("Country Successfully Edited %s" % (editedCountry.name))
            return redirect(url_for('showCountry'))
    else:
        return render_template('editCountry.html', country=editedCountry)


# To Deleting existing Country
@app.route('/country/<int:country_id>/delete/', methods=['GET', 'POST'])
def deleteCountry(country_id):
    if 'username' not in login_session:
        return redirect('/login')
    countryToDelete = session.query(Country).filter_by(id=country_id).one()
    creater_id = getUserInfo(countryToDelete.user_id)
    user_id = getUserInfo(login_session['user_id'])
    if creater_id.id != login_session['user_id']:
        flash("You cannot delete this Country "
              "This is belongs to %s" % (creater_id.name))
        return redirect(url_for('showCountry'))
    if request.method == 'POST':
        session.delete(countryToDelete)
        flash("Successfully Deleted %s" % (countryToDelete.name))
        session.commit()
        return redirect(url_for('showCountry', country_id=country_id))
    else:
        return render_template('deleteCountry.html', country=countryToDelete)


# It's Displays the total player list of partcular country
@app.route('/country/<int:country_id>/players')
def showPlayers(country_id):
    country = session.query(Country).filter_by(id=country_id).one()
    player = session.query(Player).filter_by(player_id=country_id).all()
    return render_template('menu.html', country=country, player=player)


# Creating new player
@app.route('/country/<int:player_id>/new/', methods=['GET', 'POST'])
def newPlayerList(player_id):
    if 'username' not in login_session:
        return redirect('login')
    country = session.query(Country).filter_by(id=player_id).one()
    creater_id = getUserInfo(country.user_id)
    user_id = getUserInfo(login_session['user_id'])
    if creater_id.id != login_session['user_id']:
        flash("You cannot add this player "
              "This is belongs to %s" % (creater_id.name))
        return redirect(url_for('showCountry', country_id=player_id))
    if request.method == 'POST':
        newList = Player(name=request.form['name'],
                         about=request.form['about'],
                         jersey_number=request.form['jersey_number'],
                         runs=request.form['runs'],
                         half_century=request.form['half_century'],
                         century=request.form['century'],
                         place=request.form['place'],
                         player_id=player_id,
                         user_id=login_session['user_id'])
        session.add(newList)
        session.commit()
        flash("New Player List %s is created" % (newList))
        return redirect(url_for('showPlayers', country_id=player_id))
    else:
        return render_template('newplayerlist.html', player_id=player_id)


# Editing to particular country player
@app.route('/country/<int:country_id>/<int:p_id>/edit/',
           methods=['GET', 'POST'])
def editPlayerList(country_id, p_id):
    if 'username' not in login_session:
        return redirect('/login')
    editedList = session.query(Player).filter_by(id=p_id).one()
    country = session.query(Country).filter_by(id=country_id).one()
    creater_id = getUserInfo(editedList.user_id)
    user_id = getUserInfo(login_session['user_id'])
    if creater_id.id != login_session['user_id']:
        flash("You cannot edit this Country "
              "This is belongs to %s" % (creater_id.name))
        return redirect(url_for('showPlayers', country_id=country_id))
    if request.method == 'POST':
        editedList.name = request.form['name']
        editedList.about = request.form['about']
        editedList.jersey_number = request.form['jersey_number']
        editedList.runs = request.form['runs']
        editedList.half_century = request.form['half_century']
        editedList.century = request.form['century']
        editedList.place = request.form['place']
        session.add(editedList)
        session.commit()
        flash("Player List has been edited!!")
        return redirect(url_for('showPlayers', country_id=country_id))
    else:
        return render_template('editplayerlist.html',
                               country=country, player=editedList)


# Deleting particular country of player
@app.route('/country/<int:player_id>/<int:list_id>/delete/',
           methods=['GET', 'POST'])
def deletePlayerList(player_id, list_id):
    if 'username' not in login_session:
        return redirect('/login')
    country = session.query(Country).filter_by(id=player_id).one()
    listToDelete = session.query(Player).filter_by(id=list_id).one()
    creater_id = getUserInfo(listToDelete.user_id)
    user_id = getUserInfo(login_session['user_id'])
    if creater_id.id != login_session['user_id']:
        flash("You cannot edit this Country "
              "This is belongs to %s" % (creater_id.name))
        return redirect(url_for('showPlayers', country_id=player_id))
    if request.method == 'POST':
        session.delete(listToDelete)
        session.commit()
        flash("Player list has been Deleted!!!")
        return redirect(url_for('showPlayers', country_id=player_id))
    else:
        return render_template('deleteplayerlist.html', lists=listToDelete)


# Logout from application
@app.route('/disconnect')
def logout():
    access_token = login_session['access_token']
    print("In gdisconnect access token is %s", access_token)
    print("User Name is:")
    print(login_session['username'])

    if access_token is None:
        print("Access Token is None")
        response = make_response(json.dumps('Current user not connected.'),
                                 401)
        response.headers['Content-Type'] = 'application/json'
        return response
    access_token = login_session['access_token']
    url = 'https://accounts.google.com/o/oauth2/revoke?token=%s' % access_token
    h = httplib2.Http()
    result = \
        h.request(uri=url, method='POST', body=None,
                  headers={'content-type':
                           'application/x-www-form-urlencoded'})[0]

    print result['status']
    if result['status'] == '200':
        del login_session['access_token']
        del login_session['gplus_id']
        del login_session['username']
        del login_session['email']
        del login_session['picture']
        response = make_response(json.dumps('Successfully disconnected.'), 200)
        response.headers['Content-Type'] = 'application/json'
        flash("Successfully logged out")
        return redirect(url_for('showCountry'))
    else:
        response = make_response(
            json.dumps('Failed to revoke token for given user.', 400))
        response.headers['Content-Type'] = 'application/json'
        return response

if __name__ == '__main__':
    app.secret_key = 'super_secret_key'
    app.debug = True
    app.run(host='0.0.0.0', port=5050)
