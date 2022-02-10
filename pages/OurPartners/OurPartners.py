from flask import Blueprint, render_template, redirect, url_for

# HomePage blueprint definition
OurPartners = Blueprint('OurPartners', __name__, static_folder='static', static_url_path='/OurPartners', template_folder='templates')


# Routes
@OurPartners.route('/OurPartners')
def index():
    return render_template('OurPartners.html')