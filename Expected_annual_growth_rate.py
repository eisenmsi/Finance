import yfinance as yf


def expected_annual_growth_rate(stock):
    a = yf.Ticker(stock)
    return (a.info["trailingPE"] - 8.5) / 2
