# app.py
from flask import Flask
from flask_wtf.csrf import CSRFProtect
from flask_wtf import FlaskForm
from wtforms import StringField
import os

app = Flask(__name__, static_url_path='/static')

app.config['SECRET_KEY'] = os.urandom(24)

# Initialize CSRF protection
csrf = CSRFProtect(app)

from mvc.controller import *

class ZipCodeForm(FlaskForm):
    zipCode = StringField('zipCode')

if __name__ == '__main__':
    
    app.run(debug=True)
