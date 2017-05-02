import pandas as pd
import matplotlib.pyplot as plt
import datetime
import numpy
import pylab

def describe(stock_ticker, other_tickers, start_date='1800-01-01', end_date = datetime.datetime.now().strftime("%Y-%m-%d")):
    # define date range
    dates = pd.date_range(start_date, end_date)

    # Create an empty data frame
    df1 = pd.DataFrame(index=dates)

    # read SPY dataset into temporary data frame
    dfSPY = pd.read_csv("data/{}.csv".format(stock_ticker.upper()),
                        index_col="Date",  # use Date column as Index
                        parse_dates=True,
                        usecols=["Date", "Close", "Adj Close"],  # which columns to read into dataframe
                        na_values=["NaN"])  #

    # Left join the two data frames
    df1 = df1.join(dfSPY)
    df1 = df1.dropna()
    plot_title = "{} from {} to {}".format(
        stock_ticker.upper(),
        start_date,
        end_date
    )
    df1[["Close", "Adj Close"]].plot().set_title(plot_title)

    # # plot the data itself
    # print df1
    # y = df1["Adj Close"]
    #
    # # calc the trendline
    # z = numpy.polyfit(x, y, 1)
    # p = numpy.poly1d(z)
    # pylab.plot(x, p(x), "r--")
    # # the line equation:
    # print "y=%.6fx+(%.6f)" % (z[0], z[1])

    plt.show()
