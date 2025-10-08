def knapsack_01(weights, values, capacity):
    n = len(values)
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
            if weights[i - 1] <= w:
                dp[i][w] = max(values[i - 1] + dp[i - 1][w - weights[i - 1]], dp[i - 1][w])
            else:
                dp[i][w] = dp[i - 1][w]

    w = capacity
    items_taken = []
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            items_taken.append((weights[i - 1], values[i - 1]))
            w -= weights[i - 1]
    items_taken.reverse()  # optional: maintain original order
    return dp[n][capacity], items_taken


values = [60, 100, 120]
weights = [10, 20, 30]
capacity = 50

max_value, items = knapsack_01(weights, values, capacity)

print("Maximum Value in Knapsack:", max_value)
print("Items taken (weight, value):")
for item in items:
    print(item)
