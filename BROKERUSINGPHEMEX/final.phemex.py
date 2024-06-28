# # import requests
# # import time
# # import hmac
# # import hashlib
# # import json

# # class PhemexClient:
# #     BASE_URL = "https://testnet-api.phemex.com"
# #     api_key = "4dbf6bda-8b99-4945-aa96-1753b9261df1"
# #     api_secret = "ix5bZ6NQGxirnwkPBdvRWQWm7-UEVyzenReFubGQW_YzZDlmMjM5My0xNDllLTQwMWItODc4MC00OTNlYzQ0OWIyZTU"

# #     def __init__(self, api_key, api_secret):
# #         self.api_key = api_key
# #         self.api_secret = api_secret

# #     def _create_signature(self, message):
# #         return str(hmac.new(self.api_secret.encode(), message.encode(), hashlib.sha256).hexdigest())

# #     def _send_request(self, endpoint, method="GET", params=None, data=None, signed=False):
# #         url = self.BASE_URL + endpoint
# #         headers = {
# #             "Content-Type": "application/json",
# #             "x-phemex-request-expiry": str(int(time.time()) + 60),
# #             "x-phemex-access-token": self.api_key,
# #             "x-phemex-request-signature":self._create_signature,
# #         } 
        
# #         if signed:
# #             expiry = headers["x-phemex-request-expiry"]
# #             signature_payload = f"{endpoint}{expiry}"
# #             if method == "POST" and data:
# #                 signature_payload += data
# #             headers["x-phemex-request-signature"] = self._create_signature(signature_payload)
        
# #         if method == "GET":
# #             response = requests.get(url, headers=headers, params=params)
# #         elif method == "POST":
# #             response = requests.post(url, headers=headers, data=data)
# #         elif method == "DELETE":
# #             response = requests.delete(url, headers=headers, params=params)
        
# #         return response.json()

# #     def get_server_time(self):
# #         return self._send_request("/public/time")

# #     def get_products(self):
# #         return self._send_request("/public/products")

# #     def get_klines(self, symbol):
# #         return self._send_request(f"/md/kline?symbol={symbol}&resolution=M1&limit=100")

# #     def get_order_book(self, symbol):
# #         return self._send_request(f"/md/orderbook?symbol={symbol}")

# #     def get_recent_trades(self, symbol):
# #         return self._send_request(f"/md/trade?symbol={symbol}")

# #     def place_order(self,symbol,clOrdID, side,quantity, price):
# #         data = json.dumps({
# #             "symbol": symbol,
# #             "side": side,
# #             "clOrdID": clOrdID,
# #             "priceEp": float(price),  # Price in the smallest unit
# #             "orderQty": float(quantity),  # Quantity in the smallest unit
# #         }
# #         )
# #         return self._send_request("/orders", method="POST", data=data, signed=True)

# #     def get_order(self, symbol, order_id):
# #         return self._send_request(f"/orders?symbol={symbol}&orderID={order_id}", signed=True)

# #     def get_account_balance(self):
# #         return self._send_request("/accounts/accountPositions", signed=True)

# #     def cancel_order(self, symbol, order_id):
# #         return self._send_request(f"/orders/cancel?symbol={symbol}&orderID={order_id}", method="DELETE", signed=True)

# #     def get_open_orders(self, symbol):
# #         return self._send_request(f"/orders/activeList?symbol={symbol}", signed=True)

# #     def get_all_orders(self, symbol):
# #         return self._send_request(f"/orders/all?symbol={symbol}", signed=True)

# #     def get_account_info(self):
# #         return self._send_request("/accounts/accountInfo", signed=True)

# #     def get_funding_rate(self, symbol):
# #         return self._send_request(f"/md/fundingRate?symbol={symbol}")

# #     def get_mark_price(self, symbol):
# #         return self._send_request(f"/md/markPrice?symbol={symbol}")

# #     def get_liquidation_orders(self, symbol):
# #         return self._send_request(f"/md/liquidation?symbol={symbol}")

# #     def get_income_history(self):
# #         return self._send_request("/accounts/transactions", signed=True)

# #     def get_position_risk(self):
# #         return self._send_request("/accounts/positions", signed=True)

# #     def get_commission_rate(self, symbol):
# #         return self._send_request(f"/accounts/commission?symbol={symbol}")

# #     def change_leverage(self, symbol, leverage):
# #         data = json.dumps({
# #             "symbol": symbol,
# #             "leverage": leverage,
# #         })
# #         return self._send_request("/positions/leverage", method="POST", data=data, signed=True)

# # # Example usage
# # if __name__ == "__main__":
# #     api_key = "your_api_key"
# #     api_secret = "your_api_secret"
# #     symbol = "BTCUSDT"
    
# #     client = PhemexClient(api_key, api_secret)
    
# #     print("Server time:", client.get_server_time())
# #     print("Products:", client.get_products())
# #     print("Recent trades:", client.get_recent_trades(symbol))
    
# #     order_id = client.place_order(symbol,"aryamanhjf", "Buy",0.01, 60000)
# #     print("Placed order ID:", order_id)

# #     if isinstance(order_id, str):  # Check if order_id is a valid ID string
# #         order_details = client.get_order(symbol, order_id)
# #         print("Order details:", order_details)

# #     print("Account balance:", client.get_account_balance())
# #     print("Cancel order:", client.cancel_order(symbol, order_id))
# #     print("Open orders:", client.get_open_orders(symbol))
# #     print("All orders:", client.get_all_orders(symbol))
# #     print("Account info:", client.get_account_info())
# #     print("Funding rate:", client.get_funding_rate(symbol))
# #     print("Mark price:", client.get_mark_price(symbol))
# #     print("Liquidation orders:", client.get_liquidation_orders(symbol))
# #     print("Income history:", client.get_income_history())
# #     print("Position risk:", client.get_position_risk())
# #     print("Commission rate:", client.get_commission_rate(symbol))
# #     print("Change leverage:", client.change_leverage(symbol, 20))
#     # api_key = "4dbf6bda-8b99-4945-aa96-1753b9261df1"
#     # api_secret = "ix5bZ6NQGxirnwkPBdvRWQWm7-UEVyzenReFubGQW_YzZDlmMjM5My0xNDllLTQwMWItODc4MC00OTNlYzQ0OWIyZTU"
# import requests
# import time
# import hmac
# import hashlib
# import json

# class PhemexClient:
#     BASE_URL = "https://testnet-api.phemex.com"
    
#     def __init__(self, api_key, api_secret):
#         self.api_key = api_key
#         self.api_secret = api_secret

#     def _create_signature(self, message):
#         return hmac.new(self.api_secret.encode('utf-8'), message.encode(), hashlib.sha256).hexdigest()

#     def _send_request(self, endpoint, method="GET", params=None, data=None, signed=False):
#         url = self.BASE_URL + endpoint
#         expiry = str(int(time.time()) + 60)
#         headers = {
#             "Content-Type": "application/json",
#             "x-phemex-request-expiry": expiry,
#             "x-phemex-access-token": self.api_key,
#             "x-phemex-request-signature":hmac(
                
#             )
#         }
        
#         if signed:
#             if data:
#                 data_str = json.dumps(data, separators=(',', ':'))
#             else:
#                 data_str = ''
#             signature_payload = endpoint + expiry + data_str
#             signature = self._create_signature(signature_payload)
#             headers["x-phemex-request-signature"] = signature
        
#         if method == "GET":
#             response = requests.get(url, headers=headers, params=params)
#         elif method == "POST":
#             response = requests.post(url, headers=headers, data=data_str)
#         elif method == "DELETE":
#             response = requests.delete(url, headers=headers, params=params)
        
#         return response.json()

#     def get_server_time(self):
#         return self._send_request("/public/time")

#     def get_products(self):
#         return self._send_request("/public/products")

#     def get_klines(self, symbol, resolution='M1', limit=100):
#         params = {"symbol": symbol, "resolution": resolution, "limit": limit}
#         return self._send_request("/md/kline", params=params)

#     def get_order_book(self, symbol):
#         return self._send_request("/md/orderbook", params={"symbol": symbol})

#     def get_recent_trades(self, symbol):
#         return self._send_request("/md/trade", params={"symbol": symbol})

#     def place_order(self, symbol, clOrdID, side, quantity, price):
#         data = {
#             "symbol": symbol,
#             "side": side,
#             "clOrdID": clOrdID,
#             "priceEp": int(price * 1e4),  # Price in the smallest unit
#             "orderQty": int(quantity * 1e4),  # Quantity in the smallest unit
#         }
#         return self._send_request("/orders", method="POST", data=data, signed=True)

#     def get_order(self, symbol, order_id):
#         return self._send_request(f"/orders?symbol={symbol}&orderID={order_id}", signed=True)

#     def get_account_balance(self):
#         return self._send_request("/accounts/accountPositions", signed=True)

#     def cancel_order(self, symbol, order_id):
#         return self._send_request(f"/orders/cancel?symbol={symbol}&orderID={order_id}", method="DELETE", signed=True)

#     def get_open_orders(self, symbol):
#         return self._send_request(f"/orders/activeList?symbol={symbol}", signed=True)

#     def get_all_orders(self, symbol):
#         return self._send_request(f"/orders/all?symbol={symbol}", signed=True)

#     def get_account_info(self):
#         return self._send_request("/accounts/accountInfo", signed=True)

#     def get_funding_rate(self, symbol):
#         return self._send_request(f"/md/fundingRate?symbol={symbol}")

#     def get_mark_price(self, symbol):
#         return self._send_request(f"/md/markPrice?symbol={symbol}")

#     def get_liquidation_orders(self, symbol):
#         return self._send_request(f"/md/liquidation?symbol={symbol}")

#     def get_income_history(self):
#         return self._send_request("/accounts/transactions", signed=True)

#     def get_position_risk(self):
#         return self._send_request("/accounts/positions", signed=True)

#     def get_commission_rate(self, symbol):
#         return self._send_request(f"/accounts/commission?symbol={symbol}")

#     def change_leverage(self, symbol, leverage):
#         data = {
#             "symbol": symbol,
#             "leverage": leverage,
#         }
#         return self._send_request("/positions/leverage", method="POST", data=data, signed=True)

# # Example usage
# if __name__ == "__main__":
#     api_key = "4dbf6bda-8b99-4945-aa96-1753b9261df1"
#     api_secret = "ix5bZ6NQGxirnwkPBdvRWQWm7-UEVyzenReFubGQW_YzZDlmMjM5My0xNDllLTQwMWItODc4MC00OTNlYzQ0OWIyZTU"
#     symbol = "BTCUSDT"
    
#     client = PhemexClient(api_key, api_secret)
    
#     print("Server time:", client.get_server_time())
#     print("Products:", client.get_products())
#     print("Recent trades:", client.get_recent_trades(symbol))
    
#     order_id = client.place_order(symbol, "order123", "Buy", 0.01, 60000)
#     print("Placed order ID:", order_id)

#     if isinstance(order_id, dict) and "orderID" in order_id:  # Check if order_id is a valid ID
#         order_details = client.get_order(symbol, order_id["orderID"])
#         print("Order details:", order_details)

#     print("Account balance:", client.get_account_balance())
#     print("Cancel order:", client.cancel_order(symbol, order_id["orderID"]))
#     print("Open orders:", client.get_open_orders(symbol))
#     print("All orders:", client.get_all_orders(symbol))
#     print("Account info:", client.get_account_info())
#     print("Funding rate:", client.get_funding_rate(symbol))
#     print("Mark price:", client.get_mark_price(symbol))
#     print("Liquidation orders:", client.get_liquidation_orders(symbol))
#     print("Income history:", client.get_income_history())
#     print("Position risk:", client.get_position_risk())
#     print("Commission rate:", client.get_commission_rate(symbol))
#     print("Change leverage:", client.change_leverage(symbol, 20))
# # Request Path: /orders
# # Request Query:
# # Request Body: {"symbol":"BTCUSD","clOrdID":"uuid-1573058952273","side":"Sell","priceEp":93185000,"orderQty":7,"ordType":"Limit","reduceOnly":false,"timeInForce":"GoodTillCancel","takeProfitEp":0,"stopLossEp":0}
# # Request Expiry: 1575735514
# # Signature: HMacSha256( /orders + 1575735514 + {"symbol":"BTCUSD","clOrdID":"uuid-1573058952273","side":"Sell","priceEp":93185000,"orderQty":7,"ordType":"Limit","reduceOnly":false,"timeInForce":"GoodTillCancel","takeProfitEp":0,"stopLossEp":0})
# # signed string is /orders1575735514{"symbol":"BTCUSD","clOrdID":"uuid-1573058952273","side":"Sell","priceEp":93185000,"orderQty":7,"ordType":"Limit","reduceOnly":false,"timeInForce":"GoodTillCancel","takeProfitEp":0,"stopLossEp":0}\\
import requests
import time
import hmac
import hashlib
import json

class PhemexClient:
    BASE_URL = "https://testnet-api.phemex.com"
    
    def __init__(self, api_key, api_secret):
        self.api_key = api_key
        self.api_secret = api_secret

    def _create_signature(self, message):
        return hmac.new(self.api_secret.encode('utf-8'), message.encode(), hashlib.sha256).hexdigest()

    def _send_request(self, endpoint, method="GET", params=None, data=None, signed=False):
        url = self.BASE_URL + endpoint
        expiry = str(int(time.time()) + 60)
        headers = {
            "Content-Type": "application/json",
            "x-phemex-request-expiry": expiry,
            "x-phemex-access-token": self.api_key,
            }
        
        if signed:
            if data:
                data_str = json.dumps(data, separators=(',', ':'))
            else:
                data_str = ''
            signature_payload = endpoint + expiry + data_str
            signature = self._create_signature(signature_payload)
            headers["x-phemex-request-signature"] = signature
        
        if method == "GET":
            response = requests.get(url, headers=headers, params=params)
        elif method == "POST":
            response = requests.post(url, headers=headers, data=data_str)
        elif method == "DELETE":
            response = requests.delete(url, headers=headers, params=params)
        
        return response.json()

    def get_server_time(self):
        return self._send_request("/public/time")

    def get_products(self):
        return self._send_request("/public/products")

    def get_klines(self, symbol, resolution='M1', limit=100):
        params = {"symbol": symbol, "resolution": resolution, "limit": limit}
        return self._send_request("/md/kline", params=params)

    def get_order_book(self, symbol):
        return self._send_request("/md/orderbook", params={"symbol": symbol})

    def get_recent_trades(self, symbol):
        return self._send_request("/md/trade", params={"symbol": symbol})

    def place_order(self, symbol, clOrdID, side, quantity, price):
        data = {
            "symbol": symbol,
            "side": side,
            "clOrdID": clOrdID,
            "priceEp": int(price * 1e4),  # Price in the smallest unit
            "orderQty": int(quantity * 1e4),  # Quantity in the smallest unit
        }
        # headers = {
        #     "Content-Type": "application/json",
        #     "x-phemex-request-expiry": expiry,
        #     "x-phemex-access-token": self.api_key,
        #     "x-phemex-request-signature":HMacSha256(URL Path + QueryString + Expiry + body)
        #     }
        return self._send_request("/orders", method="POST", data=data, signed=True)

    def get_order(self, symbol, order_id):
        return self._send_request(f"/orders?symbol={symbol}&orderID={order_id}", signed=True)

    def get_account_balance(self):
        return self._send_request("/accounts/accountPositions", signed=True)

    def cancel_order(self, symbol, order_id):
        return self._send_request(f"/orders/cancel?symbol={symbol}&orderID={order_id}", method="DELETE", signed=True)

    def get_open_orders(self, symbol):
        return self._send_request(f"/orders/activeList?symbol={symbol}", signed=True)

    def get_all_orders(self, symbol):
        return self._send_request(f"/orders/all?symbol={symbol}", signed=True)

    def get_account_info(self):
        return self._send_request("/accounts/accountInfo", signed=True)

    def get_funding_rate(self, symbol):
        return self._send_request(f"/md/fundingRate?symbol={symbol}")

    def get_mark_price(self, symbol):
        return self._send_request(f"/md/markPrice?symbol={symbol}")

    def get_liquidation_orders(self, symbol):
        return self._send_request(f"/md/liquidation?symbol={symbol}")

    def get_income_history(self):
        return self._send_request("/accounts/transactions", signed=True)

    def get_position_risk(self):
        return self._send_request("/accounts/positions", signed=True)

    def get_commission_rate(self, symbol):
        return self._send_request(f"/accounts/commission?symbol={symbol}")

    def change_leverage(self, symbol, leverage):
        data = {
            "symbol": symbol,
            "leverage": leverage,
        }
        return self._send_request("/positions/leverage", method="POST", data=data, signed=True)

# Example usage
if __name__ == "__main__":
    api_key = "4dbf6bda-8b99-4945-aa96-1753b9261df1"
    api_secret = "ix5bZ6NQGxirnwkPBdvRWQWm7-UEVyzenReFubGQW_YzZDlmMjM5My0xNDllLTQwMWItODc4MC00OTNlYzQ0OWIyZTU"
    symbol = "BTCUSDT"
    
    client = PhemexClient(api_key, api_secret)
    
    print("Server time:", client.get_server_time())
    print("Products:", client.get_products())
    print("Recent trades:", client.get_recent_trades(symbol))
    
    order_id = client.place_order(symbol, "order123", "Buy", 0.01, 60000)
    print("Placed order ID:", order_id)

    if isinstance(order_id, dict) and "orderID" in order_id:  # Check if order_id is a valid ID
        order_details = client.get_order(symbol, order_id["orderID"])
        print("Order details:", order_details)

    # print("Account balance:", client.get_account_balance())
    # print("Cancel order:", client.cancel_order(symbol, order_id["orderID"]))
    # print("Open orders:", client.get_open_orders(symbol))
    # print("All orders:", client.get_all_orders(symbol))
    # print("Account info:", client.get_account_info())
    # print("Funding rate:", client.get_funding_rate(symbol))
    # print("Mark price:", client.get_mark_price(symbol))
    # print("Liquidation orders:", client.get_liquidation_orders(symbol))
    # print("Income history:", client.get_income_history())
    # print("Position risk:", client.get_position_risk())
    # print("Commission rate:", client.get_commission_rate(symbol))
    # print("Change leverage:", client.change_leverage(symbol, 20))

    