import sys
import csv
import os
import Trader
from datetime import date, timedelta


def main():
    print("started... \r\n")

    companies_file = open('master_stocks_list.csv')
    companies = csv.reader(companies_file)

    totalcompanies = 0
    totalcount = 0

    valid_stocks = []

    print("Cycling through stocks... \r\n")

    for company in companies:
        ticker, company_name = company
        totalcompanies = totalcompanies + 1

        history_file = open('history/{}.csv'.format(ticker))

        reader = csv.DictReader(history_file)
        candles = list(reader)
        total_candles = len(candles)
        candles = candles[-total_candles:]

        if total_candles > 1:
            try:
                if is_bullish_engulfing(candles, total_candles - 1, company):
                    if calculate_moving_average(candles[-100:]):
                        totalcount = totalcount + 1
                        valid_stocks.append(ticker)

            except:
                pass

    invest(valid_stocks)


def is_bullish_candlestick(candle):
    return float(candle['Close']) > float(candle['Open'])


def is_bearish_candlestick(candle):
    return float(candle['Close']) < float(candle['Open'])


def is_bearish_engulfing(candles, index):
    current_day = candles[index]
    previous_day = candles[index - 1]

    if is_bullish_candlestick(previous_day) \
            and current_day['Open'] > previous_day['Close'] \
            and current_day['Close'] < previous_day['Open']:
        return True

    return False


def is_bullish_engulfing(candles, index, company):
    current_day = candles[index]
    previous_day = candles[index - 1]
    last_day = candles[index - 5]

    if is_bearish_candlestick(previous_day) \
            and float(current_day['Close']) > float(previous_day['Open']) \
            and float(current_day['Open']) < float(previous_day['Close']) \
            and float(current_day['Close']) > float(last_day['Close']):
        return True

    return False


def calculate_moving_average(candles):
    n = 0
    for candle in candles:
        n = n + float(candle['Close'])
    average = n / len(candles)

    if average > 100:
        print("Stock Passed")
        return True
    return False


def invest(stocks):
    totalvalue = 0

    for stock in stocks:
        trader = Trader.Trader(stock)
        print('trading ' + stock)
        trader.run_test()
        totalvalue = round((totalvalue + trader.total_value), 2)

    print('\n\rYou have made £{} in profit'.format(round(totalvalue - (len(stocks)*1000)), 5))

    print("Stocks Traded: ")
    for stock in stocks:
        print(stock)





if __name__ == "__main__":
    main()
