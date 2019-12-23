import requests
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import time
from datetime import datetime
from pytz import timezone
from StocksData import Stocks
import json
import pprint

caps = DesiredCapabilities().CHROME
caps["pageLoadStrategy"] = "eager"

tz = timezone('EST')
now = datetime.now(tz)


def main():

    #FOR TESTING PURPOSES, use these stocks saved in the symbols file
 #   with open("symbols.json", 'rb') as file:
 #       if file.read(2) != '[]':
 #           with open('symbols.json') as json_file:
 #               symbols = json.load(json_file)
 #               get_stocks_data(symbols)
 #       else:
            find_top_stocks()


def find_top_stocks():

    #Find the top 5 stocks in the gainers trend table. get the top 5 witht he highest amount of change
    browser = webdriver.Chrome(desired_capabilities=caps, executable_path='chromedriver')
    browser.get('https://uk.finance.yahoo.com/gainers/')

    # consent page
    consentbutton = browser.find_element_by_name('agree')
    consentbutton.click()
    # main page
    time.sleep(4)
    browser.execute_script("window.scrollTo(600, document.body.scrollHeight);")
    change = browser.find_element_by_css_selector('span[data-reactid="57"]')
    change.click()
    time.sleep(2)
    change.click()
    time.sleep(2)

    table = browser.find_element_by_css_selector('tbody[data-reactid="72"]')

    rows = table.find_elements_by_tag_name("tr")

    symbols = []
    i = 0

    while i <= 4:
        col = rows[i].find_elements_by_tag_name("td")[0]
        symbols.append(col.text)
        i = i + 1

    browser.quit()

    with open('symbols.json', 'w') as f:
        json.dump(symbols, f)

    get_stocks_data(symbols)


def get_stocks_data(symbols):
    key = 'G1523UGKW3CJ6FHH'

    with open('stock_data.json') as json_file:
        data = json.load(json_file)

        a = {
            '12:00:00': {
            }
        }

    for symbol in symbols:
        response = requests.get('https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol=' + symbol + '&apikey=' + key)
        parsed = json.loads(response.text)
        a['12:00:00'] = { symbol: [{
                'ok': parsed['Global Quote']['02. open'],
                'od': parsed['Global Quote']['03. high'],
                'ddk': parsed['Global Quote']['04. low'],
                'osdsd': parsed['Global Quote']['05. price']
                }]
            }
        json.dumps(a)
        print(json.dumps(a, indent=4, sort_keys=True))

        with open('stock_data.json', 'w') as outfile:
            json.dump(a, outfile)

    #distinguish bullish engulfing pattern



def buy_stock(stock):
    print("buying " + stock)


def sell_stock(stock):
    print("selling " + stock)


if __name__ == "__main__":
    main()
