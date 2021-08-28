import pandas_datareader as web


def average_return(stock, year, duration=20, time="Y"):
    begin = year - duration
    start = str(begin) + "-12-25"
    end = str(year) + "-12-25"
    a = web.get_data_yahoo(stock, start, end)
    returns = a['Adj Close'].resample(time).ffill().pct_change()[1:]
    return returns.mean()


def std_return(stock, year, duration=20, time="Y"):
    begin = year - duration
    start = str(begin) + "-12-25"
    end = str(year) + "-12-25"
    a = web.get_data_yahoo(stock, start, end)
    returns = a['Adj Close'].resample(time).ffill().pct_change()[1:]
    return returns.std()


def corr_return(stock, year, duration=20, time="D"):
    begin = year - duration
    start = str(begin) + "-12-25"
    end = str(year) + "-12-25"
    a = web.get_data_yahoo(stock, start, end)
    returns = a['Adj Close'].resample(time).ffill().pct_change()[1:]
    return returns.corr()
