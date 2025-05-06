from flask import Flask, jsonify
import csv
from datetime import datetime

app = Flask(__name__)

@app.route("/price")
def get_price():
    with open("prices.csv", "r") as file:
        reader = csv.reader(file)
        prices = list(reader)
    latest_price = prices[-1][1] if prices else "N/A"
    return jsonify({"price": latest_price})

if __name__ == "__main__":
    app.run(debug=True)