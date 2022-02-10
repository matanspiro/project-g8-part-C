from flask import Blueprint, render_template

AboutUs = Blueprint('AboutUs', __name__, static_folder='static', static_url_path='/AboutUs', template_folder='templates')


# Routes
@AboutUs.route('/AboutUs')
def index():
    return render_template('AboutUs.html')
