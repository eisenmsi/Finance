from Alpha_and_Beta import *
from Stock_Returns import *

stock = "MCHP"
market = "SPY"

pe_ratio = {2019: 58.75, 2018: 230, 2017: 83.04, 2016: 110.4, 2015: 24.39, 2014: 23.82, 2013: 49.24, 2012: 21.5,
            2011: 16.57, 2010: 23.09, 2009: 20.58, 2008: 19.19, 2007: 22.76}
pe_ratio_market = {2019: 19.60, 2018: 24.97, 2017: 23.59, 2016: 22.18, 2015: 20.02, 2014: 18.15, 2013: 17.03,
                   2012: 14.87, 2011: 16.30, 2010: 20.70, 2009: 70.91, 2008: 21.46, 2007: 17.36, 2006: 18.07,
                   2005: 19.99, 2004: 22.73, 2003: 31.43, 2002: 46.17, 2001: 27.55, 2000: 29.04, 1999: 32.92,
                   1998: 24.29, 1997: 19.53, 1996: 18.08, 1995: 14.89}

for i in range(2020, 1994, -1):
    print(str(average_return(stock, i, duration=1)) + ", " + str(average_return(stock, i - 1, duration=1)) + ", " + str(
        average_return(market, i, duration=1)) + ", " + str(average_return(market, i - 1, duration=1)) + ", " + str(
        pe_ratio[i - 1]) + ", " + str(pe_ratio_market[i - 1]) + ", " + str(
        alpha_beta_stock(stock, i - 1)[0]) + ", " + str(alpha_beta_stock(stock, i - 1)[1]))
