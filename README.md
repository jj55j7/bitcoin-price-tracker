# Bitcoin Price Tracker 

A real-time Bitcoin price monitor that:
- Fetches prices from CoinGecko API
- Displays them in a web interface
- Updates every 5 seconds

## Features
- Live price updates
- Simple Flask backend
- Clean frontend interface

## How to Run
1. Clone the repo:
   ```bash
   git clone https://github.com/your-username/bitcoin-price-tracker.git
   ```
2. Install dependencies:
   ```bash
   pip install flask requests
   ```
3. Run the services:
   ```bash
   # Terminal 1 - Data fetcher
   python crypto.py
   
   # Terminal 2 - Flask server
   python server.py
   ```
4. Open `http://localhost:5000` in your browser

## Tech Stack
- Python (Flask backend)
- JavaScript (Frontend)
- CoinGecko API

## Future Improvements
- [ ] Add price history chart
- [ ] Support multiple cryptocurrencies
- [ ] Deploy to cloud
