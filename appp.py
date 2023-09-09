from flask import Flask, request, jsonify
from geopy.geocoders import Nominatim
import requests
from requests.auth import HTTPBasicAuth
#register_url = 'https://api2.watttime.org/v2/register'
#params = {'username': 'foster',
#        'password': 'stay_woke#99',
#       'email': 'fostrnilsson99@gmail.com',
#         'org': 'fosters app'}
#rsp = requests.post(register_url, json=params)
#print(rsp.text)
  
  
  #### login and get API token ####
login_url = 'https://api2.watttime.org/v2/login'
rsp = requests.get(login_url, auth=HTTPBasicAuth('foster', 'stay_woke#99'))
print(rsp.json())

def get_lat_long_from_zip(zipcode):
    geolocator = Nominatim(user_agent="myGeoZone")
    location = geolocator.geocode(zipcode + ", USA")
    if location:
        return location.latitude, location.longitude
    else:
        return None

@app.route('/api/convert-zip', methods=['POST'])
def convert_zip():
    data = request.get_json()
    zip_code = data.get('zipCode')

    if not zip_code:
        return jsonify({'error': 'ZIP code error, try a different one near your zip'}), 400

    coordinates = get_lat_long_from_zip(zip_code)
    if coordinates:
        latitude, longitude = coordinates

        # Pass latitude and longitude as parameters to the function
        region_info = get_region_info(latitude, longitude)
        return jsonify(region_info)
    else:
        return jsonify({'error': 'Invalid ZIP code'}), 400

def get_region_info(latitude, longitude):
    region_url = 'https://api2.watttime.org/v2/ba-from-loc'
    token = requests.get(login_url, auth=HTTPBasicAuth('foster', 'stay_woke#99')).json()['token']
    headers = {'Authorization': 'Bearer {}'.format(token)}
    params = {'latitude': str(latitude), 'longitude': str(longitude)}
    
    rsp = requests.get(region_url, headers=headers, params=params)
    
    if rsp.status_code == 200:
        return {'region_info': rsp.text}
    else:
        return {'error': 'An error occurred while fetching region information'}

if __name__ == '__main__':
    app.run()