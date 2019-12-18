import json

class Stocks:
    def __init__(self, stockname, stockopen, high, low, price, timestamp):

        self.stockname = stockname
        self.stockopen = stockopen
        self.high = high
        self.low = low
        self.price = price
        self.timestamp = timestamp

        #load json
        with open('stock_data.json') as json_file:
            data = json.load(json_file)

        #add data
        data['Stocks'].update({timestamp: {stockname: {"open": stockopen, "high": high, "low": low, "price": price}}})

        # #write back to file
        with open('stock_data.json', 'w') as outfile:
            json.dump(data, outfile)