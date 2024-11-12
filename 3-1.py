def max_profit(prices):
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
prices = 0 # body
res = max_profit(prices)
