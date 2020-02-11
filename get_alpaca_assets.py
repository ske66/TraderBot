import requests, json

api_key = 'PKJMB4IWG9R6WSA1YQRS'
private_key = 'pQ2Lec7oHlDcRCI8QNSTvzsyzXZlPS180V3MEY4v'

BASE_URL = 'https://paper-api.alpaca.markets'
ASSETS_URL = '{}/v2/assets'.format(BASE_URL)
ORDERS_URL = '{}/v2/orders'.format(BASE_URL)
HEADERS = { 'APCA-API-KEY-ID': api_key, 'APCA-API-SECRET-KEY': private_key }

def get_assets():
    response = requests.get(ASSETS_URL, headers=HEADERS)
    return json.loads(response.content)


def create_order(symbol, qty, side, type, time_in_force):
    data = {
        "symbol": symbol,
        "qty": qty,
        "side": side,
        "type": type,
        "time_in_force": time_in_force
    }

    response = requests.post(ORDERS_URL, json=data, headers=HEADERS)

    return json.loads(response.content)

response = create_order("ANSS", "100", "buy", "market", "day")

print(response)
