from flask import request, jsonify, redirect, url_for, session, Flask
from myapp import app
from mvc.model import ZipCodeModel
from mvc.view import ZipCodeForm, render_template, render_index, render_result

@app.route('/', methods=['GET', 'POST'])
def index():
    form = ZipCodeForm()
    return render_index(form)

@app.route('/get-csrf-token')
def get_csrf_token():
    csrf_token = csrf._get_token()
    if csrf_token:
        return jsonify({'csrf_token': csrf_token})
    else:
        return jsonify({'error': 'CSRF token not found'})    

@app.route('/submit', methods=['GET','POST'])
def submit():
    zip_code = request.form.get('zipCode')
    selected_appliances = request.form.getlist('appliances[]')

    # Process the form data and prepare the result_data
    result_data = {
        'zipCode': zip_code,
        'appliances': selected_appliances,
        # Add other data you want to include in the response
    }

    # Save result_data in the session
    session['result_data'] = result_data

    # Redirect to the /result route
    return jsonify({'redirect': url_for('result', _external=True)})

@app.route('/result', methods=['GET','POST'])  # Use GET method for rendering result
def result():
    # Retrieve result_data from the session
    result_data = session.get('result_data')

    # Ensure result_data exists in the session
    if result_data is None:
        return 'Result data not found.'

    # Render the template with result_data
    return render_template('result.html', result_data=result_data)
    