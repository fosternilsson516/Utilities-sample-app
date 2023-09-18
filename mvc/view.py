# view.py
from flask import render_template
from wtforms import StringField
from flask_wtf import FlaskForm  # Import FlaskForm from flask_wtf

class ZipCodeForm(FlaskForm):
    zipCode = StringField('zipCode')

def render_index(form, appliances):
    return render_template('index.html', form=form, appliances=appliances)

def render_output(zip_code, selected_appliances):
    return render_template('result.html', zip_code=zip_code, selected_appliances=selected_appliances)    

