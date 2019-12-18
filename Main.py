import requests
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import time
from datetime import datetime
from pytz import timezone
from StocksData import Stocks
import json
import sys

caps = DesiredCapabilities().CHROME
caps["pageLoadStrategy"] = "eager"

tz = timezone('EST')
now = datetime.now(tz)


def main():

    #at 10:30 am Eastern Time get the top 5 highest changed gainer stocks

    #load all data from the previous session and load the money available (*0.75) into the program

    #then, make calls to each stock every minute.

    find_top_stocks()


def find_top_stocks():

    print("Scrape scrape scrape")

    browser = webdriver.Chrome(desired_capabilities=caps,executable_path='/Users/markbarton/Downloads/chromedriver')
    browser.get('https://uk.finance.yahoo.com/gainers/')

    #consent page
    consentbutton = browser.find_element_by_name('agree')
    consentbutton.click()

    #main page
    time.sleep(4)
    change = browser.find_element_by_css_selector('span[data-reactid="57"]')
    change.click()
    time.sleep(2)
    change.click()
    time.sleep(2)

    table = browser.find_element_by_css_selector('tbody[data-reactid="72"]')

    rows = table.find_elements_by_tag_name("tr")

    symbols = []
    i = 4

    while i <= 4:
        col = rows[i].find_elements_by_tag_name("td")[0]
        symbols.append(col.text)
        i = i+1


    time.sleep(10)
    browser.quit()

    get_stocks_data(symbols)


def get_stocks_data(symbols):

    key = 'G1523UGKW3CJ6FHH'

    time = now.strftime("%H:%M:%S")

    for symbol in symbols:
        response = requests.get('https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol=' + symbol + '&apikey=' + key)
        parsed = json.loads(response.text)
        stock = Stocks(parsed["Global Quote"]["01. symbol"], parsed["Global Quote"]["02. open"], parsed["Global Quote"]["03. high"], parsed["Global Quote"]["04. low"], parsed["Global Quote"]["05. price"], now.strftime("%H:%M:%S"))


def buy_stock(stock):
    print("buying " + stock)




def sell_stock(stock):
    print("selling " + stock)





if __name__ == "__main__":
    main()
