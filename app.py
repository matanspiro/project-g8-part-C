from flask import Flask

###### App setup
app = Flask(__name__)
app.config.from_pyfile('settings.py')

###### Pages
## AboutUs
from pages.AboutUs.AboutUs import AboutUs
app.register_blueprint(AboutUs)

## Checkout
from pages.Checkout.Checkout import Checkout
app.register_blueprint(Checkout)

## ContactUs
from pages.ContactUs.ContactUs import ContactUs
app.register_blueprint(ContactUs)

## FAQ
from pages.FAQ.FAQ import FAQ
app.register_blueprint(FAQ)

## HomePage
from pages.HomePage.HomePage import HomePage
app.register_blueprint(HomePage)

## Login
from pages.Login.Login import Login
app.register_blueprint(Login)

## OurPartners
from pages.OurPartners.OurPartners import OurPartners
app.register_blueprint(OurPartners)

## PrivacyPolicy
from pages.PrivacyPolicy.PrivacyPolicy import PrivacyPolicy
app.register_blueprint(PrivacyPolicy)

## Products
from pages.Products.Products import Products
app.register_blueprint(Products)

## Register
from pages.Register.Register import Register
app.register_blueprint(Register)

## PersonalInfo
from pages.PersonalInfo.PersonalInfo import PersonalInfo
app.register_blueprint(PersonalInfo)

## Page error handlers
#from pages.page_error_handlers.page_error_handlers import page_error_handlers
#app.register_blueprint(page_error_handlers)


if __name__ == '__main__':
    app.run(debug=True)
