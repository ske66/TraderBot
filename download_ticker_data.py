import yfinance as yf
import csv
from datetime import datetime, timedelta

def download_data(assets):
    count = 0
    row_count = len(assets)

    five_days = (datetime.now() - timedelta(5)).strftime('%Y-%m-%d')
    today = (datetime.now() - timedelta(0)).strftime('%Y-%m-%d')

    for asset in assets:
        count += 1

        if 'DELISTED' not in asset['symbol']:
            try:
                history_filename = 'history/{}.csv'.format(asset['symbol'])

                f = open(history_filename, 'w', newline='')
                ticker = yf.Ticker(asset['symbol'])
                df = ticker.history(start=five_days, end=today)
                f.write(df.to_csv())
                f.close()
            except:
                pass


        percentage = float("{0:.2f}".format(100*(count / row_count)))
        decimalised = str(percentage)
        print(decimalised + "% complete")


