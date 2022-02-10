from flask import Blueprint, render_template, redirect, url_for, request, session, flash
from utilities.Classes.user import User

Login = Blueprint('Login', __name__, static_folder='static', static_url_path='/Login', template_folder='templates')

@Login.route('/Login')
def index():
    return render_template('Login.html')


@Login.route('/Connect', methods=['POST'])
def connect():
    email = request.form['user_name']
    password = request.form['psw']
    user = User('a', 'a', 'a', 'a', 'a')  # no need to create new user
    user_id = user.get_user_id(email)
    name = user.get_name(email, password)  # check if it's the correct password
    session['Name'] = name  # return user's name from DB
    if name == "":
        flash('Please Register Before You Sign In')
        return redirect('/Login')
    elif name == "wrong_psw":
        flash('Wrong Password - Please Try Again')
        return redirect('/Login')
    session['user_name'] = email
    session['user_id'] = user_id
    return redirect('/')


@Login.route('/Logout', methods=['POST'])
def logout():
    del session['user_name']
    del session['user_id']
    return redirect('/')
