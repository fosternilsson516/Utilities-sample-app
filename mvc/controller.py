from flask import request, jsonify
from myapp import app
from mvc.model import ZipCodeModel
from mvc.view import render_application, render_resume, ZipCodeForm, render_index

@app.route('/')
def index():
    return render_index()

@app.route('/resume.html')
def resume():
    return render_resume()

@app.route('/get-csrf-token')
def get_csrf_token():
    csrf_token = csrf._get_token()
    if csrf_token:
        return jsonify({'csrf_token': csrf_token})
    else:
        return jsonify({'error': 'CSRF token not found'})    

@app.route('/application.html', methods=['GET', 'POST'])
def application():
    form = ZipCodeForm()
    selected_appliances = []
    return render_application(form, selected_appliances)

@app.route('/', methods=['POST'])
def post_zip():
    if request.method == 'POST':
        zip_code = request.form.get('zipCode')
        selected_appliances = request.form.getlist('appliances[]')
        result = ZipCodeModel.process_zip(zip_code)
        return jsonify(result)


