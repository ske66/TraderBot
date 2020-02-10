import os
import requests
import json

api_key = 'PKJMB4IWG9R6WSA1YQRS'
private_key = 'pQ2Lec7oHlDcRCI8QNSTvzsyzXZlPS180V3MEY4v'

base_url = 'https://paper-api.alpaca.markets'

endpoint = '{}/v2/assets'.format(base_url)

r = requests.get(endpoint, headers={'APCA-API-KEY-ID': api_key, 'APCA-API-SECRET-KEY': private_key})

parsed = r.json()

stock_list = []

for stock in parsed:
    stock_list.append(stock['symbol'])
    print(stock['symbol'])

print('Total stocks: ' + str(len(stock_list)))
