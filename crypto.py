import requests
import time
import csv
from datetime import datetime
import os

def get_bitcoin_price():
    try:
        url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd"
        response = requests.get(url)
        data = response.json()
        return data["bitcoin"]["usd"]
    except:
        print("API Error: Retrying in 10 seconds...")
        time.sleep(10)  # Wait longer if API fails
        return get_bitcoin_price()  # Retry

def log_price(price):
    file_path = "prices.csv"
    with open(file_path, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([datetime.now().strftime("%H:%M:%S"), price])
    print(f"Logged price to: {os.path.abspath(file_path)}")  # Print full file path

# Replace this:
# with open("prices.csv", "a") as file:
#     pass

# With this:
with open("prices.csv", "w", newline="") as file:  # 'w' overwrites, creates if missing
    writer = csv.writer(file)
    writer.writerow(["Time", "Price"])  # Write header

while True:
    price = get_bitcoin_price()
    log_price(price)
    print(f"[{datetime.now().strftime('%H:%M:%S')}] Bitcoin Price: ${price}")
    time.sleep(5)  # Check every 5 seconds