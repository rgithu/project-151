month = ("january","feburary","March","April","May","June","July","August", "September","October","November","December")
profits = (2400,3000,200,500,300,2500,4000,2100,2200,2300,2400,2900)

max_profit=max(profits)
print(max_profit)
max_profit_index=profits.index(max_profit)
print(max_profit_index)

max_profit_month = month[max_profit_index]
print("The maximum profit was in "+str(max_profit_month)+" and the profit value is "+str(max_profit))

min_profit=min(profits)
print(min_profit)
min_profit_index=profits.index(min_profit)
print(min_profit_index)

min_profit_month= month[min_profit_index]
print("The minimum profit was in "+str(min_profit_month)+" and the minimum profit value is "+str(min_profit))

