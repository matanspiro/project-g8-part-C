from flask import Blueprint, render_template, redirect, url_for, request, session, flash

from utilities.Classes.eventPar import eventPar
from utilities.Classes.user import User
from utilities.Classes.donation import donation

PersonalInfo = Blueprint('PersonalInfo', __name__, static_folder='static',
                         static_url_path='/PersonalInfo', template_folder='templates')

user = User('a', 'a', 'a', 'a', 'a')
@PersonalInfo.route('/PersonalInfo')
def index():
    return render_template('PersonalInfo.html')

@PersonalInfo.route('/updateProfile', methods=['post'])
def updateProfile_func():
    isUpdated = False
    email = session['user_name']
    user_id = user.get_user_id(email)
    if request.form['RegName'] and request.form['RegName'] != "":
        newFullName = request.form['RegName']
        user.update_userName(user_id, newFullName)
        isUpdated = True

    if request.form['email'] and request.form['email'] != "":
        newEmail = request.form['email']
        user.update_userEmail(user_id, newEmail)
        isUpdated = True

    if request.form['PhoneNum'] and request.form['PhoneNum'] != "":
        newPhone = request.form['PhoneNum']
        user.update_userPhone(user_id, newPhone)
        isUpdated = True

    if request.form['psw'] and request.form['psw'] != "":
        newPass = request.form['psw']
        user.update_userPass(user_id, newPass)
        isUpdated = True

    if isUpdated:
        flash("Updated successfully")

    return redirect('/PersonalInfo')


@PersonalInfo.route('/checkIfRSVPed', methods=['post'])
def checkEvents_func():
    participant = eventPar(0, 0, 'a')
    user_id = session['user_id']
    usersEvents = participant.checkEvents(user_id)
    if usersEvents:
        return render_template('PersonalInfo.html', eventsData=usersEvents)
    flash("No events have been booked yet")
    return render_template('PersonalInfo.html')

@PersonalInfo.route('/unRSVP', methods=['post'])
def unRSVP_func():
    participant2 = eventPar(0, 0, 'a')
    user_id = session['user_id']
    event_id = request.form['EventID']
    isDeleted = participant2.delete_ParFromEvent(user_id, event_id)
    if isDeleted:
        flash("Unsubscribed from event successfully")
        return redirect('/PersonalInfo')
    else:
        flash("Failed to unsubscribed from event")
        return redirect('/PersonalInfo')


@PersonalInfo.route('/wantToUpdate', methods=['get'])
def wantToUpdate():
    return render_template('PersonalInfo.html', wantToUpdateInfo=True)


@PersonalInfo.route('/checkOrders', methods=['post'])
def checkOrders_func():
    Donation = donation('a', 'a', 'a', 0)
    user_id = session['user_id']
    usersDonations = Donation.donations_history(user_id)
    if usersDonations:
        total=Donation.user_total_donation(user_id)
        return render_template('PersonalInfo.html', amount=total)
    flash("No donations received yet")
    return render_template('PersonalInfo.html')