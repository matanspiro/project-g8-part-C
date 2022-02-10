from datetime import datetime
from flask import Blueprint, render_template, redirect, url_for, request, flash, session
from utilities.Classes.eventPar import eventPar, get_events

HomePage = Blueprint('HomePage', __name__, static_folder='static', static_url_path='/HomePage', template_folder='templates')

@HomePage.route('/')
def index():
    return render_template('HomePage.html')

@HomePage.route('/homepage')
@HomePage.route('/home')
def redirect_homepage():
    return redirect(url_for('HomePage.index'))

@HomePage.route('/AhimGdolimEvent')
def AhimGdolimEvent():
    if get_events():
        allEvents = get_events()
    else:
        flash("Bad output")
    return render_template('AhimGdolimEvent.html', Event=allEvents)

@HomePage.route('/MahiaEvent')
def MahiaEventEvent():
    allEvents = get_events()
    return render_template('MahiaEvent.html', Event=allEvents)

@HomePage.route('/SurvivorsEvent')
def SurvivorsEvent():
    allEvents = get_events()
    return render_template('SurvivorsEvent.html', Event=allEvents)

@HomePage.route('/LevinstheinEvent')
def LevinshteinEvent():
    allEvents = get_events()
    return render_template('LevinstheinEvent.html', Event=allEvents)


@HomePage.route('/check_par_Ahim', methods=['post'])
def check_par_Ahim_func():
    someEvent = eventPar(0, 0, 'a')
    event = request.form['AhimGdolimID']  # takes the value (Event_id) from html
    capStatus = someEvent.spaceStatus(event)
    if capStatus:  # there's space
        participant = eventPar(0, 0, 'a')
        user_id = session['user_id']
        usersEvents = participant.checkEvents(user_id)
        alreadyRegistered = False
        for i in range(0, len(usersEvents)):
            if (usersEvents[i][0]) == int(event):
                alreadyRegistered = True
                break
        if not alreadyRegistered:
            build_par = eventPar(event, session['user_id'], datetime.now().strftime('%Y-%m-%d-%H:%M:%S'))
            build_par.insert_par()
            flash('Registration to the event succeeded')
        else:
            flash('You have already registered to this event')

    else:
        flash('Event is already full - try a different event')
    return render_template('AhimGdolimEvent.html')

@HomePage.route('/check_par_Mahia', methods=['post'])
def check_par_Mahia_func():
    someEvent = eventPar(0, 0, 'a')
    event = request.form['MahiaID']  # takes the value (Event_id) from html
    capStatus = someEvent.spaceStatus(event)
    if capStatus:  # there's space
        participant = eventPar(0, 0, 'a')
        user_id = session['user_id']
        usersEvents = participant.checkEvents(user_id)
        alreadyRegistered = False
        for i in range(0, len(usersEvents)):
            if (usersEvents[i][0]) == int(event):
                alreadyRegistered = True
                break
        if not alreadyRegistered:
            build_par = eventPar(event, session['user_id'], datetime.now().strftime('%Y-%m-%d-%H:%M:%S'))
            build_par.insert_par()
            flash('Registration to the event succeeded')
        else:
            flash('You have already registered to this event')
    else:
        flash('Event is already full - try a different event')
    return render_template('MahiaEvent.html')

@HomePage.route('/check_par_Survivors', methods=['post'])
def check_par_Survivors_func():
    someEvent = eventPar(0, 0, 'a')
    event = request.form['SurvivorsID']  # takes the value (Event_id) from html
    capStatus = someEvent.spaceStatus(event)
    if capStatus:  # there's space
        participant = eventPar(0, 0, 'a')
        user_id = session['user_id']
        usersEvents = participant.checkEvents(user_id)
        alreadyRegistered = False
        for i in range(0, len(usersEvents)):
            if (usersEvents[i][0]) == int(event):
                alreadyRegistered = True
                break
        if not alreadyRegistered:
            build_par = eventPar(event, session['user_id'], datetime.now().strftime('%Y-%m-%d-%H:%M:%S'))
            build_par.insert_par()
            flash('Registration to the event succeeded')
        else:
            flash('You have already registered to this event')
    else:
        flash('Event is already full - try a different event')
    return render_template('SurvivorsEvent.html')

@HomePage.route('/check_par_Levinshtein', methods=['post'])
def check_par_Levinshtein_func():
    someEvent = eventPar(0, 0, 'a')
    event = request.form['LevinshteinID']  # takes the value (Event_id) from html
    capStatus = someEvent.spaceStatus(event)
    if capStatus:  # there's space
        participant = eventPar(0, 0, 'a')
        user_id = session['user_id']
        usersEvents = participant.checkEvents(user_id)
        alreadyRegistered = False
        for i in range(0, len(usersEvents)):
            if (usersEvents[i][0]) == int(event):
                alreadyRegistered = True
                break
        if not alreadyRegistered:
            build_par = eventPar(event, session['user_id'], datetime.now().strftime('%Y-%m-%d-%H:%M:%S'))
            build_par.insert_par()
            flash('Registration to the event succeeded')
        else:
            flash('You have already registered to this event')
    else:
        flash('Event is already full - try a different event')
    return render_template('LevinstheinEvent.html')
