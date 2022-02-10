from flask import Blueprint, render_template, redirect, url_for

# HomePage blueprint definition
FAQ = Blueprint('FAQ', __name__, static_folder='static', static_url_path='/FAQ', template_folder='templates')


# Routes
@FAQ.route('/FAQ')
def index():
    return render_template('FAQ.html')
