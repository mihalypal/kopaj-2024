

def max_profit(prices):
    prices = prices[1:-1]
    prices = prices.split(', ')
    prices = [int(x) for x in prices]
    print(prices)
    min_price = float('inf')
    max_profit = 0
    buy_day = 0
    sell_day = 0
    
    for i in range(len(prices)):
        if prices[i] < min_price:
            min_price = prices[i]
            buy_day = i
        current_profit = prices[i] - min_price
        if current_profit > max_profit:
            max_profit = current_profit
            sell_day = i
    
    return (buy_day, sell_day)

# Example usage:
prices = '[1236, 333, 913, 1335, 149, 1769, 1939, 1290, 789, 358]'
res = max_profit(prices)
print(res)