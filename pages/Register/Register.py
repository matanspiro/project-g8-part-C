from flask import Blueprint, render_template, redirect, url_for, request, flash

from utilities.Classes.user import User

Register = Blueprint('Register', __name__, static_folder='static', static_url_path='/Register', template_folder='templates')


@Register.route('/Register')
def index():
    return render_template('Register.html')


@Register.route('/insert_user', methods=['POST'])
def insert():
    user = User('Name', 'BirthDate', 'Email', 'Phone_Number', 'Password')
    name = request.form['RegName']
    birthDate = request.form['Bday']
    email = request.form['email']
    phoneNumber = request.form['PhoneNum']
    user_email = user.get_email(email)
    if user_email:
        password = request.form['psw']
        user = User(name, birthDate, email, phoneNumber, password)
        user.insert_user()
        flash('Registration succeeded')
    else:
        flash('User with the same email already exists')
    register = "yes"
    return render_template('Register.html', register=register)
