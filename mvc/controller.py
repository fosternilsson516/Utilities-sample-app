from flask import request, jsonify, redirect, url_for
from myapp import app
from mvc.model import ZipCodeModel
from mvc.view import ZipCodeForm, render_index, render_template

@app.route('/', methods=['GET', 'POST'])
def index():
    form = ZipCodeForm()
    appliances = []
    return render_index(form, appliances)

@app.route('/get-csrf-token')
def get_csrf_token():
    csrf_token = csrf._get_token()
    if csrf_token:
        return jsonify({'csrf_token': csrf_token})
    else:
        return jsonify({'error': 'CSRF token not found'})    

@app.route('/submit', methods=['POST'])
def submit():
    zip_code = request.form.get('zipCodeInput')
    selected_appliances = request.form.getlist('appliances[]')

    # Process the zip code and selected appliances here

    # Redirect to the result page and pass the input data as parameters
    return redirect(url_for('result', zip_code=zip_code, selected_appliances=selected_appliances))

@app.route('/result')
def result():
    zip_code = request.args.get('zip_code')
    selected_appliances = request.args.getlist('selected_appliances')
    return render_template('result.html', zip_code=zip_code, selected_appliances=selected_appliances)
    # Process the zip code and selected appliances here

    # Redirect to the result page and pass the input data as parameters
    return redirect(url_for('result', zip_code=zip_code, selected_appliances=selected_appliances))