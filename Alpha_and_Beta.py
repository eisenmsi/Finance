import pandas_datareader as web
from scipy import stats


def alpha_beta_portfolio(stock, weights, year, duration=5):
    begin = year - duration
    start = str(begin) + "-12-25"
    end = str(year) + "-12-25"
    price_data = web.get_data_yahoo(stock, start, end)
    ret_data = price_data['Adj Close'].resample("M").ffill().pct_change()[1:]
    port_ret = (ret_data * weights).sum(axis=1)
    benchmark_price = web.get_data_yahoo('SPY', start, end)
    benchmark_ret = benchmark_price["Adj Close"].resample("M").ffill().pct_change()[1:]
    (beta, alpha) = stats.linregress(benchmark_ret.values, port_ret.values)[0:2]
    return alpha, beta


def alpha_beta_stock(stock, year, duration=5):
    begin = year - duration
    start = str(begin) + "-12-25"
    end = str(year) + "-12-25"
    price_data = web.get_data_yahoo(stock, start, end)
    ret_data = price_data['Adj Close'].resample("M").ffill().pct_change()[1:]
    benchmark_price = web.get_data_yahoo('SPY', start, end)
    benchmark_ret = benchmark_price["Adj Close"].resample("M").ffill().pct_change()[1:]
    (beta, alpha) = stats.linregress(benchmark_ret.values, ret_data.values)[0:2]
    return alpha, beta
