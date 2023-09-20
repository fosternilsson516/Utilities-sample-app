from flask import request, jsonify, redirect, url_for
from myapp import app
from mvc.model import ZipCodeModel
from mvc.view import ZipCodeForm, render_template, render_index, render_output

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
    
        zip_code = request.form.get('zipCode')
        selected_appliances = request.form.getlist('appliances[]')

        # Process the zip code and selected appliances here
        result_data = ZipCodeModel.process_data(zip_code, selected_appliances)

        # Return a JSON response with the result and selected appliances
        #return jsonify(result=result_data["result"], appliances=result_data["appliances"])

        #return redirect(url_for('result', zip_code=zip_code, selected_appliances=selected_appliances))
        return redirect(url_for('result', result=result_data))

@app.route('/result')
def result():
    result_data = request.args.get('result')
    return render_template('result.html', result=result_data)
    #zip_code = request.args.get('zip_code')
    #selected_appliances = request.args.getlist('selected_appliances')
    #return render_template('result.html', zip_code=zip_code, selected_appliances=selected_appliances)
    # Process the zip code and selected appliances here

    # Redirect to the result page and pass the input data as parameters
    #return redirect(url_for('result', zip_code=zip_code, selected_appliances=selected_appliances))