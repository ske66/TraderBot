import yfinance as yf
import sys
import csv
from datetime import date, timedelta


def main():
    print("started... \r\n")

    companies_file = open('russell100_companies.csv')
    companies = csv.reader(companies_file)

    for company in companies:

        ticker, company_name = company

        history_file = open('history/{}.csv'.format(ticker))

        reader = csv.DictReader(history_file)
        candles = list(reader)

        if len(candles[-5:]) > 1:
            if is_bullish_engulfing(candles[-5:], 4):

                check_moving_average(candles, 1)


                print('{} has a previous day close of {} and a close of {} on {}'.format(ticker,
                                                                                         candles[-2]['Close'],
                                                                                         candles[1]['Close'],
                                                                                         candles[1]['Date']))
                invest(ticker)


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


def is_bullish_engulfing(candles, index):
    current_day = candles[index]
    previous_day = candles[index - 1]
    second_day = candles[index - 2]
    third_day = candles[index - 3]
    forth_day = candles[index - 4]

    if is_bearish_candlestick(previous_day) \
            and float(current_day['Close']) > float(previous_day['Open']) \
            and float(current_day['Close']) > float(second_day['Close']) \
            and float(current_day['Close']) > float(third_day['Close']) \
            and float(current_day['Close']) > float(forth_day['Close']) \
            and float(current_day['Open']) < float(previous_day['Close']):
        return True

    return False



def check_moving_average(candles, index):

    print("current day: " + candles[0])
    print("last day: " + candles[index - 2])

    #print("got it")




def invest(stocks):
    print('trading ' + stocks)


if __name__ == "__main__":
    main()
