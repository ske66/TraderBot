import yfinance as yf
import csv

# https://stackoverflow.com/questions/25338608/download-all-stock-symbol-list-of-a-market

count = 0

companies = csv.reader(open('master_stocks_list.csv'))

row_count = 3621 #sum(1 for row in companies)  # fileObject is your csv.reader

for company in companies:
    count += 1

    symbol, name = company

    history_filename = 'history/{}.csv'.format(symbol)

    f = open(history_filename, 'w', newline='')

    ticker = yf.Ticker(symbol)

    df = ticker.history(period="1y")

    f.write(df.to_csv())

    f.close()

    percentage = float("{0:.2f}".format(100*(count / row_count)))

    decimalised = str(percentage)

    print(decimalised + "% complete")


