import requests
import os

def fetch_stock_data(stock_ticker):
    url = "https://chart.finance.yahoo.com/table.csv?s={}&a=0&b=29&c=1800&d=4&e=1&f=2017&g=d&ignore=.csv".format(stock_ticker.upper())
    response = requests.get(url, {})
    if response.content.find("<html>") > -1:
        print "Invalid Stock Symbol: {}".format(stock_ticker.upper())
    else:
        file_path = "./data/{}.csv".format(stock_ticker.upper())
        if os.path.isfile(file_path):
            print "Already Collected Data for {}".format(stock_ticker.upper())
        else:
            file_descriptor = open(file_path, "w")
            file_descriptor.write(response.content)
            print "Successfully Collected Data for {}".format(stock_ticker.upper())

def head(stock_ticker, response):
    print "Data for {}".format(stock_ticker)
    lines = response.content.split()
    for i in range(10):
        print lines[i]
    print "... {} more lines".format(len(lines) - 10)
