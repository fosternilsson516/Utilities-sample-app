# view.py
from flask import render_template
from wtforms import StringField
from flask_wtf import FlaskForm  # Import FlaskForm from flask_wtf

class ZipCodeForm(FlaskForm):
    zipCode = StringField('zipCode')

def render_index():
    return render_template('index.html')

def render_resume():
    return render_template('resume.html')

def render_application(form, selected_appliances):
    return render_template('application.html', form=form)
