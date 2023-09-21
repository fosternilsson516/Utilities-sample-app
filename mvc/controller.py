from flask import request, jsonify, redirect, url_for
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

    # Return a JSON response with the result and selected appliances
    result_data = {
        'zipCode': zip_code,
        'appliances': selected_appliances,
        # Add other data you want to include in the response
    }
    return jsonify(result_data)
    
        

@app.route('/result', methods=['POST'])
def result():
    zip_code = request.args.get('zipCode')
    selected_appliances = request.args.getlist('appliances[]')

    zip_code_data = ZipCodeModel.zip_code_data(zip_code)
    selected_appliances_data = ZipCodeModel.selected_appliances_data(selected_appliances)

    return render_template('result.html', zip_code=zip_code_data, selected_appliances=selected_appliances_data)
    

    # Redirect to the result page and pass the input data as parameters
    #return redirect(url_for('result', zip_code=zip_code, selected_appliances=selected_appliances))