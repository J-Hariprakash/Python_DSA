def stock(prices):
    l  = len(prices)
    mini = prices[0]
    profit = 0
    for i in range(1,l):
        total = prices[i] - mini
        profit = max(profit,total)
        mini = min(prices[i],mini)
    return profit
size = int(input("Enter Required Size for an array: \n"))
prices = []
for i in range(size):
    elmts = int(input("Enter elements required: \n"))
    prices.append(elmts)     
result = stock(prices)
print("maximum profit :",result)