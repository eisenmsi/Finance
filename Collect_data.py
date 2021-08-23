import Alpha_and_Beta
import Info
import Stock_Returns

stock = "ADDYY"
print(Info.stock_info(stock))
for i in range(2020, 2004, -1):
    # print(Stock_Returns.average_return(stock, i, duration=1))
    print(Alpha_and_Beta.alpha_beta_stock(stock, i)[0] + ", " + Alpha_and_Beta.alpha_beta_stock(stock, i)[1])
