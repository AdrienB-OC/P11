import json
from flask import Flask,render_template,request,redirect,flash,url_for
from datetime import datetime


def loadClubs():
    with open('clubs.json') as c:
         listOfClubs = json.load(c)['clubs']
         return listOfClubs


def loadCompetitions():
    with open('competitions.json') as comps:
         listOfCompetitions = json.load(comps)['competitions']
         return listOfCompetitions


def edit_club(club_data):
    clubs_dict = {}
    with open('clubs') as c:
        clubs = json.load(c)['clubs']
        for club in clubs:
            if club['email'] == club_data['email']:
                club['points'] = club_data['points']
    with open('clubs', 'w') as c:
        clubs_dict['clubs'] = clubs
        json.dump(clubs_dict, c, indent=4)


def edit_competition(competition_data):
    comps_dict = {}
    with open('competitions') as c:
        comps = json.load(c)['competitions']
        for comp in comps:
            if comp['name'] == competition_data['name']:
                comp['numberOfPlaces'] = competition_data['numberOfPlaces']
    with open('competitions', 'w') as c:
        comps_dict['competitions'] = comps
        json.dump(comps_dict, c, indent=4)


def create_app(config):
    app = Flask(__name__)
    app.secret_key = 'something_special'
    app.config.from_object(config)
    competitions = loadCompetitions()
    clubs = loadClubs()
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    @app.route('/')
    def index():
        return render_template('index.html')

    @app.route('/showSummary',methods=['POST'])
    def showSummary():
        try:
            club = [club for club in clubs
                    if club['email'] == request.form['email']][0]
            return render_template('welcome.html', club=club,
                                   competitions=competitions,
                                   time=current_time)
        except IndexError:
            flash("Error : Unregistered email")
            return render_template('index.html')


    @app.route('/book/<competition>/<club>')
    def book(competition,club):
        try:
            foundClub = [c for c in clubs if c['name'] == club][0]
            foundCompetition = [c for c in competitions
                                if c['name'] == competition][0]
        except IndexError:
            foundClub = None
            foundCompetition = None
        if foundClub and foundCompetition:
            return render_template('booking.html', club=foundClub,
                                   competition=foundCompetition)
        else:
            flash("Something went wrong-please try again")
            return render_template('welcome.html', club=club,
                                   competitions=competitions,
                                   time=current_time)


    @app.route('/purchasePlaces',methods=['POST'])
    def purchasePlaces():
        competition = [c for c in competitions
                       if c['name'] == request.form['competition']][0]
        club = [c for c in clubs if c['name'] == request.form['club']][0]
        placesRequired = int(request.form['places'])

        if placesRequired > 12:
            flash('You can only book up to 12 places')
            return render_template('welcome.html', club=club,
                                   competitions=competitions,
                                   time=current_time)
        if placesRequired > int(club['points']):
            flash('Not enough points')
            return render_template('welcome.html', club=club,
                                   competitions=competitions,
                                   time=current_time)

        competition['numberOfPlaces'] = int(competition['numberOfPlaces'])-placesRequired
        club['points'] = int(club['points']) - placesRequired
        competition['numberOfPlaces'] = str(competition['numberOfPlaces'])
        club['points'] = str(club['points'])
        # Remove commentary to update JSON DB files when executing
        # edit_club(club)
        # edit_competition(competition)
        flash('Great-booking complete!')
        return render_template('welcome.html', club=club, competitions=competitions,
                                   time=current_time)

    @app.route('/points')
    def points_display():
        return render_template('points.html', clubs=clubs)


    @app.route('/logout')
    def logout():
        return redirect(url_for('index'))

    return app
