from flask import Blueprint, render_template, redirect, url_for

# HomePage blueprint definition
PrivacyPolicy = Blueprint('PrivacyPolicy', __name__, static_folder='static', static_url_path='/PrivacyPolicy', template_folder='templates')


# Routes
@PrivacyPolicy.route('/PrivacyPolicy')
def index():
    return render_template('PrivacyPolicy.html')
