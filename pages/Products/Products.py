from flask import Blueprint, render_template, redirect, url_for, session,request, flash
from utilities.Classes.donation import donation
from utilities.Classes.user import User
from utilities.Classes.checkOut import Check_out

# HomePage blueprint definition
Products = Blueprint('Products', __name__, static_folder='static', static_url_path='/Products', template_folder='templates')

user = User('a', 'a', 'a', 'a','a')
Donation = donation('a','a','a',0)


# Routes
@Products.route('/Products',methods=['GET', 'POST'])
def index():
    if session.get('user_name'):
        email = session['user_name']
        user_id = user.get_user_id(email)
        open_donations = Donation.open_donations(user_id)
        if open_donations:
            print('has open donations')
        else:
            return render_template('Products.html', no_donations=True)
    return render_template('Products.html')


@Products.route('/Products/FoodBasket', methods=['GET'])
def insert_food_Basket():
    if session:
        email = session['user_name']
        user_id = user.get_user_id(email)
        if 'amountNum1' in request.args:
            quantity = request.args['amountNum1']
            quantity = int(quantity)
            Donation = donation('a','a','a',0)
            product_open_donations = Donation.open_donations_by_product(user_id, 1)
            if product_open_donations:
                old_quantity = Donation.get_quntity(user_id, 1)
                old_quantity = int(old_quantity)
                Donation.update_product_quantity(user_id, 1, quantity+old_quantity)
            else:
                Donation.insert_to_donations(1, user_id, quantity, 0)
            return redirect(url_for('Products.index'))
    return redirect(url_for('Products.index'))


@Products.route('/Products/PillowsAndBlankets', methods=['GET'])
def insert_pillows_and_blankets():
    if session:
        email = session['user_name']
        user_id = user.get_user_id(email)
        if 'amountNum2' in request.args:
            quantity = request.args['amountNum2']
            quantity = int(quantity)
            Donation = donation('a','a','a',0)
            product_open_donations = Donation.open_donations_by_product(user_id, 4)
            if product_open_donations:
                old_quantity = Donation.get_quntity(user_id, 4)
                old_quantity = int(old_quantity)
                Donation.update_product_quantity(user_id, 4, quantity + old_quantity)
            else:
                Donation.insert_to_donations(4, user_id, quantity, 0)
            return redirect(url_for('Products.index'))
    return redirect(url_for('Products.index'))


@Products.route('/Products/HotFood', methods=['GET'])
def insert_hot_food():
    if session:
        email = session['user_name']
        user_id = user.get_user_id(email)
        if 'amountNum3' in request.args:
            quantity = request.args['amountNum3']
            quantity = int(quantity)
            Donation = donation('a','a','a',0)
            product_open_donations = Donation.open_donations_by_product(user_id, 2)
            if product_open_donations:
                old_quantity = Donation.get_quntity(user_id, 2)
                old_quantity = int(old_quantity)
                Donation.update_product_quantity(user_id, 2, quantity + old_quantity)
            else:
                Donation.insert_to_donations(2, user_id, quantity, 0)
            return redirect(url_for('Products.index'))
    return redirect(url_for('Products.index'))


@Products.route('/Products/PotsAndPans', methods=['GET'])
def insert_pots_and_pans():
    if session:
        email = session['user_name']
        user_id = user.get_user_id(email)
        if 'amountNum4' in request.args:
            quantity = request.args['amountNum4']
            quantity = int(quantity)
            Donation = donation('a','a','a',0)
            product_open_donations = Donation.open_donations_by_product(user_id, 5)
            if product_open_donations:
                old_quantity = Donation.get_quntity(user_id, 5)
                old_quantity = int(old_quantity)
                Donation.update_product_quantity(user_id, 5, quantity + old_quantity)
            else:
                Donation.insert_to_donations(5, user_id, quantity, 0)
            return redirect(url_for('Products.index'))
    return redirect(url_for('Products.index'))


@Products.route('/Products/Candies', methods=['GET'])
def insert_candies():
    if session:
        email = session['user_name']
        user_id = user.get_user_id(email)
        if 'amountNum5' in request.args:
            quantity = request.args['amountNum5']
            quantity = int(quantity)
            Donation = donation('a','a','a',0)
            product_open_donations = Donation.open_donations_by_product(user_id, 3)
            if product_open_donations:
                old_quantity = Donation.get_quntity(user_id, 3)
                old_quantity = int(old_quantity)
                Donation.update_product_quantity(user_id, 3, quantity + old_quantity)
            else:
                Donation.insert_to_donations(3, user_id, quantity, 0)
            return redirect(url_for('Products.index'))
    return redirect(url_for('Products.index'))


@Products.route('/Products/Pajamas', methods=['GET'])
def insert_pajamas():
    if session:
        email = session['user_name']
        user_id = user.get_user_id(email)
        if 'amountNum6' in request.args:
            quantity = request.args['amountNum6']
            quantity = int(quantity)
            Donation = donation('a','a','a',0)
            product_open_donations = Donation.open_donations_by_product(user_id, 6)
            if product_open_donations:
                old_quantity = Donation.get_quntity(user_id, 6)
                old_quantity = int(old_quantity)
                Donation.update_product_quantity(user_id, 6, quantity + old_quantity)
            else:
                Donation.insert_to_donations(6, user_id, quantity, 0)
            return redirect(url_for('Products.index'))
    return redirect(url_for('Products.index'))


@Products.route('/Products/100NIS', methods=['GET'])
def insert_100NIS():
    if session:
        email = session['user_name']
        user_id = user.get_user_id(email)
        Donation = donation('a','a','a',0)
        product_open_donations = Donation.open_donations_by_product(user_id, 7)
        if product_open_donations:
            old_quantity = Donation.get_quntity(user_id, 7)
            old_quantity = int(old_quantity)
            Donation.update_product_quantity(user_id, 7, 1 + old_quantity)
        else:
            Donation.insert_to_donations(7, user_id, 1, 0)
        return redirect(url_for('Products.index'))
    return redirect(url_for('Products.index'))


@Products.route('/Products/200NIS', methods=['GET'])
def insert_200NIS():
    if session:
        email = session['user_name']
        user_id = user.get_user_id(email)
        Donation = donation('a','a','a',0)
        product_open_donations = Donation.open_donations_by_product(user_id, 9)
        if product_open_donations:
            old_quantity = Donation.get_quntity(user_id, 9)
            old_quantity = int(old_quantity)
            Donation.update_product_quantity(user_id, 9, 1 + old_quantity)
        else:
            Donation.insert_to_donations(9, user_id, 1, 0)
        return redirect(url_for('Products.index'))
    return redirect(url_for('Products.index'))


@Products.route('/Products/OtherPrice', methods=['GET'])
def insert_other_price():
    if session:
        email = session['user_name']
        user_id = user.get_user_id(email)
        if 'amountOFcash' in request.args:
            quantity = request.args['amountOFcash']
            quantity = int(quantity)
            Donation = donation('a','a','a',0)
            product_open_donations = Donation.open_donations_by_product(user_id, 8)
            if product_open_donations:
                old_quantity = Donation.get_quntity(user_id, 8)
                old_quantity = int(old_quantity)
                Donation.update_product_quantity(user_id, 8, quantity + old_quantity)
            else:
                Donation.insert_to_donations(8, user_id, quantity, 0)
            return redirect(url_for('Products.index'))
    return redirect(url_for('Products.index'))


@Products.route('/Products/ResetChoices')
def reset_choices():
    if session:
        email = session['user_name']
        user_id = user.get_user_id(email)
        Donation = donation('a', 'a', 'a', 0)
        Donation.delete_choices(user_id)
        return redirect(url_for('Products.index'))
    return redirect(url_for('Products.index'))

@Products.route('/Products/Proceed2Checkout')
def proceed_2_checkout():
    if session:
        email = session['user_name']
        user_id = user.get_user_id(email)
        checkout = Check_out('a', 'a', 'a', 'a', 'a', 'a')
        choices = checkout.user_choices(user_id)
        total_price = checkout.user_total_price(user_id)
        return render_template('Checkout.html', choices=choices, total_price=total_price)
    return redirect(url_for('HomePage.index'))


