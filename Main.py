import csv
import download_ticker_data
import get_alpaca_assets


def main():
    print("started... \r\n")
    print("pulling stocks data:")

    assets = get_alpaca_assets.get_assets()
    download_ticker_data.download_data(assets)

    totalcount = 0

#
 #   for company in assets:
#
 #       history_file = open('history/{}.csv'.format(company))
#
 #       reader = csv.DictReader(history_file)
  #      candles = list(reader)
   #     total_candles = len(candles)
    #    candles = candles[-total_candles:]
#
 #       if total_candles > 1:
  #          try:
   #             if is_bullish_engulfing(candles, total_candles - 1, company):
    #                totalcount = totalcount + 1
     #       except:
      #          pass


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


if __name__ == "__main__":
    main()
