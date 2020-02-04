import yfinance as yf
import csv

companies = csv.reader(open('russell100_companies.csv'))

for company in companies:
    print(company)

    symbol, name = company

    history_filename = 'history/{}.csv'.format(symbol)

    f = open(history_filename, 'w', newline='')

    ticker = yf.Ticker(symbol)

    df = ticker.history(period="1y")

    f.write(df.to_csv())

    f.close()
