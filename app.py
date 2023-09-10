from flask import Flask, request, jsonify, session, render_template, url_for
from flask_wtf.csrf import CSRFProtect
from flask_wtf import FlaskForm
from wtforms import StringField
import os

app = Flask(__name__, static_url_path='/static')

app.config['SECRET_KEY'] = os.urandom(24)

# Initialize CSRF protection
csrf = CSRFProtect(app)

class ZipCodeForm(FlaskForm):
    zipCode = StringField('zipCode')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/resume.html')
def resume():
    return render_template('resume.html')

@app.route('/application.html')
def application():
    # Create a form instance and render it with the CSRF token
    form = ZipCodeForm()
    return render_template('application.html', form=form)

@app.route('/get-csrf-token')
def get_csrf_token():
    # Retrieve the CSRF token from the session
    csrf_token = csrf._get_token()
    if csrf_token:
        return jsonify({'csrf_token': csrf_token})
    else:
        return jsonify({'error': 'CSRF token not found'})      

@app.route('/', methods=['POST'])
def process_zip():
   if request.method == 'POST':
        # Process the zip code data here
        zip_code = request.form.get('zipCode')
        # Perform some logic or return a response
        result = {"result": "Processed data for zip code: " + zip_code}
        return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
