from flask import Flask, jsonify
from flask_cors import CORS
import json

app = Flask(__name__)
CORS(app)

@app.route('/fetch')
def fetch():
    with open('../data.json') as file:
        data = json.load(file)

    transports = data['transport']
    cities = set()

    for transport in transports:
        city = transport['city']
        if city not in cities:
            cities.add(city)

    return jsonify(sorted((list(cities))))

@app.route('/<string:destiny>')
def searchTrip(destiny):
    with open('../data.json') as file:
        data = json.load(file)
    transports = data['transport']

    filtered_transports = []
    
    for transport in transports:
        if transport['city'] == destiny:
            filtered_transports.append(transport)

    comfort = max(filtered_transports, key=lambda x: float(x["price_confort"].replace("R$ ", "").replace(",", ".")))
    econ = min(filtered_transports, key=lambda x: float(x["price_econ"].replace("R$ ", "").replace(",", ".")))

    results = {
        "comfort": comfort, 
        "econ": econ
    }

    return results

if __name__ == '__main__':
    app.run(port=3000, debug=True)
