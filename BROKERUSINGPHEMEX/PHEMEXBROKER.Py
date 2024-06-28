import requests
import time
import hmac
import hashlib
import json
import json
import requests
import time
import hmac
import hashlib
import json
import uuid

# Replace with your testnet API credentials
API_KEY = '34f3acce-92a9-4bfd-a692-d4d80041c371'
API_SECRET = 'PEvPJ5IPvLnlqVc0qgjsnZ6e8sNyGrKMtAdMXip3c4RlOGM1MTRlNS04NzJhLTQzYTYtYTBiYS1hZDJjZWVmOGZjMTk'
BASE_URL = 'https://testnet-api.phemex.com'

def sign_request(method, endpoint, params, api_secret):
    expiry = int(time.time()) + 60
    payload = f"{method}{endpoint}{expiry}"
    if params:
        payload += json.dumps(params)
    signature = hmac.new(api_secret.encode('utf-8'), payload.encode('utf-8'), hashlib.sha256).hexdigest()
    return signature, expiry

def place_order(symbol, side, order_qty, price_ep, order_type='Limit', cl_ord_id=None, reduce_only=False, time_in_force='GoodTillCancel', take_profit_ep=0, stop_loss_ep=0):
    if cl_ord_id is None:
        cl_ord_id = "DSLKFLSKDJF"  # Generate a unique clOrdID if not provided
    
    endpoint = '/orders'
    url = BASE_URL + endpoint
    method = 'POST'
    params = {
        "symbol": symbol,
        "clOrdID": cl_ord_id,
        "side": side,  # "Buy" or "Sell"
        "priceEp": price_ep,  # Price in integer format
        "orderQty": order_qty,
        "ordType": order_type,  # "Limit" or "Market"
        "reduceOnly": reduce_only,
        "timeInForce": time_in_force,
        "takeProfitEp": take_profit_ep,
        "stopLossEp": stop_loss_ep
    }

    signature, expiry = sign_request(method, endpoint, params, API_SECRET)
    
    headers = {
        'x-phemex-access-token': API_KEY,
        'x-phemex-request-signature': signature,
        'x-phemex-request-expiry': str(expiry),
        'Content-Type': 'application/json'
    }
    
    response = requests.post(url, headers=headers, data=json.dumps(params))
    return response.json()

# Example usage
symbol = 'BTCUSD'
side = 'Sell'
order_qty = 7  # Amount you want to sell
price_ep = 93185000  # Price in Ep format
order_type = 'Limit'  # Use 'Market' for market orders
reduce_only = False
time_in_force = 'GoodTillCancel'
take_profit_ep = 0
stop_loss_ep = 0

response = place_order(symbol, side, order_qty, price_ep, order_type, reduce_only=reduce_only, time_in_force=time_in_force, take_profit_ep=take_profit_ep, stop_loss_ep=stop_loss_ep)
print(response)
