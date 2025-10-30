def maximumProfit(prices):
    # Initialize the minimum price with the first element of the list.
    # This represents the lowest price we've seen so far (to buy).
    min_price = prices[0]
    
    # Initialize maximum profit as 0 because initially, no transaction is made.
    max_profit = 0
    
    # Get the total number of price entries.
    n = len(prices)
    
    # Loop through all prices one by one.
    for i in range(0, n):
        # Update the minimum price if the current price is lower.
        # This means we found a cheaper stock to buy.
        min_price = min(min_price, prices[i])
        
        # Calculate potential profit if we sell at the current price.
        # Then, update max_profit if this profit is greater than previous ones.
        max_profit = max(max_profit, prices[i] - min_price)
        
        # Optional (for understanding): you can print intermediate steps
        # print(f"Day {i}: Price = {prices[i]}, Min Price = {min_price}, Max Profit = {max_profit}")
    
    # Finally, print the maximum profit found.
    print(f"The Maximum Profit Is {max_profit}")


# Example list of prices for each day
prices = [9, 6, 1, 3, 6, 8, 11]

# Call the function to compute the maximum profit
maximumProfit(prices)

