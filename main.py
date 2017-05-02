import pandas as pd
import matplotlib.pyplot as plt
import collector
import describer
import datetime

def main():
    # Get Input
    tckr = raw_input("Enter a Stock Symbol: ")
    other_tckrs = raw_input("Enter Related Stock Symbols (comma separated): ")
    other_tckrs = other_tckrs.split(",")
    other_tckrs = filter(None, other_tckrs)

    # Collect Data
    collector.fetch_stock_data(tckr)
    for ot in other_tckrs:
        collector.fetch_stock_data(ot)

    # Analyze
    # All Time
    describer.describe(tckr, other_tckrs)


    # Year
    now = datetime.datetime.now()
    year_ago = now - datetime.timedelta(days=365)
    start_date = year_ago.strftime("%Y-%m-%d")
    end_date = now.strftime("%Y-%m-%d")
    describer.describe(tckr, other_tckrs, start_date, end_date)


    # 3 Months
    three_months_ago = now - datetime.timedelta(days=90)
    start_date = three_months_ago.strftime("%Y-%m-%d")
    describer.describe(tckr, other_tckrs, start_date, end_date)

    # todo: relative close price of related companies
    # todo: headlines (+ links) to information about given company

if __name__ == "__main__":
    main()
