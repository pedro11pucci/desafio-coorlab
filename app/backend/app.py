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

if __name__ == '__main__':
    app.run(port=3000, debug=True)
