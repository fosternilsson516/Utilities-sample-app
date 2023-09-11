# view.py
from flask import render_template

def render_index():
    return render_template('index.html')

def render_resume():
    return render_template('resume.html')

def render_application(form):
    return render_template('application.html', form=form)