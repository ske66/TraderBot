import yfinance as yf
import csv
from datetime import datetime, timedelta

# https://stackoverflow.com/questions/25338608/download-all-stock-symbol-list-of-a-market

count = 0

companies = csv.reader(open('master_stocks_list.csv'))

row_count = 3621 #sum(1 for row in companies)  # fileObject is your csv.reader

year = (datetime.now() - timedelta(365)).strftime('%Y-%m-%d')

today = (datetime.now() - timedelta(0)).strftime('%Y-%m-%d')

for company in companies:
    count += 1

    symbol, name = company

    history_filename = 'history/{}.csv'.format(symbol)

    f = open(history_filename, 'w', newline='')

    ticker = yf.Ticker(symbol)

    df = ticker.history(start=year, end=today)

    f.write(df.to_csv())

    f.close()

    percentage = float("{0:.2f}".format(100*(count / row_count)))

    decimalised = str(percentage)

    print(decimalised + "% complete")


