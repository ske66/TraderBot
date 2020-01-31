import yfinance as yf
import sys
import csv

def main():

    stock = "MSFT"
    stockTicker = yf.Ticker(stock)
    dataFrame = stockTicker.history(period="1y")

    print(dataFrame.to_csv())


if __name__ == "__main__":

    main()