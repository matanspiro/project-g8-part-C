from flask import Blueprint, render_template, redirect, url_for, session, request
from utilities.Classes.donation import donation
from utilities.Classes.user import User
from utilities.Classes.checkOut import Check_out

Checkout = Blueprint('Checkout', __name__, static_folder='static', static_url_path='/Checkout', template_folder='templates')

user = User('a', 'a', 'a', 'a', 'a')
check_out = Check_out('a', 'a', 'a', 'a', 'a', 'a')

@Checkout.route('/Checkout')
def index():
    return render_template('Checkout.html')

@Checkout.route('/PayDonation', methods=['GET', 'POST'])
def pay_donation():
    if session:
        email = session['user_name']
        user_id = user.get_user_id(email)
        # if 'cardNum' in request.args:

        cc_number = request.form['cardNum']
        holder_id = request.form['holder_id']
        exp_month = request.form['expireMonth']
        exp_year = request.form['expireYear']
        cvc = request.form['CVC']
        exist = check_out.check_if_CC_exists(cc_number)
        if exist:
            print('exist')
        else:
            check_out.insert_credit_card(cc_number, user_id, holder_id, exp_month, exp_year, cvc)
        check_out.update_ordered(user_id)
        return redirect(url_for('HomePage.index'))
    return redirect(url_for('HomePage.index'))
