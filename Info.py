import Stock_Returns
import Expected_annual_growth_rate
import Alpha_and_Beta

import yfinance as yf


def stock_info(stock):
    a = yf.Ticker(stock)
    return a.info


def current_price(stock):
    a = yf.Ticker(stock)
    return a.info["currentPrice"]


def return_on_assets(stock):
    a = yf.Ticker(stock)
    return a.info["returnOnAssets"]


def debt_to_equity(stock):
    a = yf.Ticker(stock)
    return a.info["debtToEquity"]


def total_cash(stock):
    a = yf.Ticker(stock)
    return a.info["totalCash"]


def total_debt(stock):
    a = yf.Ticker(stock)
    return a.info["totalDebt"]


def total_cash_per_share(stock):
    a = yf.Ticker(stock)
    return a.info["totalCashPerShare"]


def revenue_per_share(stock):
    a = yf.Ticker(stock)
    return a.info["revenuePerShare"]


def book_value(stock):
    a = yf.Ticker(stock)
    return a.info["bookValue"]


def held_percent_institutions(stock):
    a = yf.Ticker(stock)
    return a.info["heldPercentInstitutions"]


def price_to_book(stock):
    a = yf.Ticker(stock)
    return a.info["priceToBook"]


def beta(stock):
    a = yf.Ticker(stock)
    return a.info["beta"]


def peg_ratio(stock):
    a = yf.Ticker(stock)
    return a.info["pegRatio"]


def forward_pe_ratio(stock):
    a = yf.Ticker(stock)
    return a.info["forwardPE"]


def dividend_rate(stock):
    a = yf.Ticker(stock)
    return a.info["dividendRate"]


def trailing_pe_ratio(stock):
    a = yf.Ticker(stock)
    return a.info["trailingPE"]


def financials(stock):
    a = yf.Ticker(stock)
    return a.financials


def dividends(stock):
    a = yf.Ticker(stock)
    return a.dividends


def actions(stock):
    a = yf.Ticker(stock)
    return a.actions


def major_holders(stock):
    a = yf.Ticker(stock)
    return a.major_holders


def balance_sheet(stock):
    a = yf.Ticker(stock)
    return a.balance_sheet


def cashflow(stock):
    a = yf.Ticker(stock)
    return a.cashflow


def earnings(stock):
    a = yf.Ticker(stock)
    return a.earnings


def sustainability(stock):
    a = yf.Ticker(stock)
    return a.sustainability


def recommendations(stock):
    a = yf.Ticker(stock)
    return a.recommendations


def get_info_stock(stock, year):
    print("Stock: " + stock)
    print("Average return: " + str(Stock_Returns.average_return(stock, year)))
    print("Standard deviation: " + str(Stock_Returns.std_return(stock, year)))
    print("Expected annual growth rate: " + str(Expected_annual_growth_rate.expected_annual_growth_rate(stock)))
    print("Alpha: " + str(Alpha_and_Beta.alpha_beta_stock(stock, year)[0]))
    print("Beta: " + str(Alpha_and_Beta.alpha_beta_stock(stock, year)[1]) + ", " + str(beta(stock)))
    print("Current price: " + str(current_price(stock)))
    print("Debt to equity: " + str(debt_to_equity(stock)))
    print("Total cash: " + str(total_cash(stock)))
    print("Total debt: " + str(total_debt(stock)))
    print("Revenue per share: " + str(revenue_per_share(stock)))
    print("Book value: " + str(book_value(stock)))
    print("Institutions: " + str(held_percent_institutions(stock)))
    print("Price to book: " + str(price_to_book(stock)))
    print("PEG ratio: " + str(peg_ratio(stock)))
    print("Forward PE ratio: " + str(forward_pe_ratio(stock)))
    print("Trailing PE ratio: " + str(trailing_pe_ratio(stock)))
    print("Dividend rate: " + str(dividend_rate(stock)))
    print(financials(stock))
    print(earnings(stock))
    print(sustainability(stock))
    print(recommendations(stock))


def get_info_portfolio(portfolio, weights, year):
    print("Average return: " + str(Stock_Returns.average_return(portfolio, year)))
    print("Standard deviation: " + str(Stock_Returns.std_return(portfolio, year)))
    print("Correlation: ")
    print(Stock_Returns.corr_return(portfolio, year))
    print("Alpha: " + str(Alpha_and_Beta.alpha_beta_portfolio(portfolio, weights, year)[0]))
    print("Beta: " + str(Alpha_and_Beta.alpha_beta_portfolio(portfolio, weights, year)[1]))
