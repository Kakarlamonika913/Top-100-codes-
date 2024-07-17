def max_profit(prices):
    n = len(prices)
    if n < 2:
        return 0
    profit_before = [0] * n
    profit_after = [0] * n
    min_price = prices[0]
    for i in range(1, n):
        min_price = min(min_price, prices[i])
        profit_before[i] = max(profit_before[i-1], prices[i] - min_price)
    max_price = prices[-1]
    for i in range(n-2, -1, -1):
        max_price = max(max_price, prices[i])
        profit_after[i] = max(profit_after[i+1], max_price - prices[i])
    max_profit = 0
    for i in range(n):
        max_profit = max(max_profit, profit_before[i] + profit_after[i])
    
    return max_profit
prices = [3, 3, 5, 0, 0, 3, 1, 4]
print(max_profit(prices))  # Output: 6
