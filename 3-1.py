def max_profit(prices):
    # Initialize variables for the best profit, buy day, and sell day
    min_price = float('inf')  # Start with a very high value for the minimum price
    max_profit = 0            # Start with zero profit
    buy_day = 0               # Initialize buy day
    sell_day = 0              # Initialize sell day
    
    # Iterate through the list of prices
    for i in range(len(prices)):
        # If we find a new minimum price, update the buy day
        if prices[i] < min_price:
            min_price = prices[i]
            buy_day = i
            
        # Calculate the potential profit if selling at prices[i]
        current_profit = prices[i] - min_price
        
        # If the current profit is higher than the max profit, update the max profit and sell day
        if current_profit > max_profit:
            max_profit = current_profit
            sell_day = i
    
    return (buy_day, sell_day)

# Example usage:
prices = [17, 11, 60, 25, 150, 75, 31, 120]
print(max_profit(prices))  # Output should be (1, 4)
