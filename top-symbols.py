import requests

# URL for Nifty Next 50 index data
nifty_next_50_url = 'https://www.nseindia.com/api/stockIndices?index=NIFTY_50'

# Headers to simulate a request from a standard web browser (avoiding the block)
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
    'Accept-Language': 'en-US,en;q=0.9',
    'Accept-Encoding': 'gzip, deflate, br',
    'Connection': 'keep-alive'
}

# Send GET request with custom headers
response = requests.get(nifty_next_50_url, headers=headers)

# Check for successful response (status code 200)
if response.status_code == 200:
    # Parse the JSON response to get symbols
    nifty_next_50_symbols = [stock['symbol'] for stock in response.json()['data']]
    
    # Print the Nifty Next 50 symbols
    print("Nifty Next 50 symbols:")
    for symbol in nifty_next_50_symbols:
        print(symbol)
else:
    print(f"Failed to fetch data. HTTP Status Code: {response.status_code}")
