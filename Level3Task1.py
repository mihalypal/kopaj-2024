def max_profit(prices):
    if not prices or len(prices) != 7:
        raise ValueError("The list must contain 7 prices, one for each day of the week.")

    min_price = prices[0]
    min_day = 0
    max_profit = 0
    buy_day = 0
    sell_day = 0

    for i in range(1, len(prices)):
        if prices[i] < min_price:
            min_price = prices[i]
            min_day = i
        elif prices[i] - min_price > max_profit:
            max_profit = prices[i] - min_price
            buy_day = min_day
            sell_day = i

    return buy_day, sell_day

# Example usage
prices = [17, 11, 60, 25, 150, 75, 31]
print(max_profit(prices))  # Output: (1, 4)
