def getMaximumProfit(price, profit):
    n = len(price)
    
    if n < 3:
        return -1  # Not enough days for a valid triplet

    max_profit = [-1] * n  # Initialize an array to store maximum profit ending on each day

    for i in range(n):
        for j in range(i):
            if price[i] > price[j]:
                max_profit[i] = max(max_profit[i], profit[i] + profit[j])

    total_max_profit = -1

    for i in range(n):
        for j in range(i):
            if price[i] > price[j] and max_profit[j] != -1:
                total_max_profit = max(total_max_profit, max_profit[j] + profit[i])

    return total_max_profit

# Example usage
if __name__ == '__main__':
    price = [1, 5, 3, 4, 6]
    profit = [2, 3, 4, 5, 6]
    result = getMaximumProfit(price, profit)
    print(result)  # Output should be 15