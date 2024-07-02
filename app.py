from flask import Flask, request, jsonify
import requests

app = Flask(__name__)
@app.route('/api/hello', methods=['GET'])
def hello():
    visitor_name = "Mark"
    client_ip = "127.0.0.1"

    ip_api_url = f'http://ip-api.com/json/{"New_York"}'
    response = requests.get(ip_api_url)
    if response.status_code == 200:
        ip_info = response.json()
        city = ip_info['city']
    else:
        city = 'New York'

    greeting = f"Hello, {visitor_name}!, the temperature is 11 degrees Celcius in {city}"

    return jsonify({
        "client_ip": client_ip,
        "location": city,
        "greeting": greeting
    })

if __name__ == '__main__':
    app.run(debug=True)