# view.py
from flask import render_template
from wtforms import StringField, FieldList
from flask_wtf import FlaskForm  # Import FlaskForm from flask_wtf

class ZipCodeForm(FlaskForm):
    zipCode = StringField('zipCode')
    appliances = FieldList(StringField('appliances[]'))

def render_index(form):
    return render_template('index.html', form=form)

def render_result(zip_code, selected_appliances):
    return render_template('result.html', zip_code=zip_code, selected_appliances=selected_appliances)    

