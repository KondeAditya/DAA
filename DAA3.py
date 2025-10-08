def fractional_knapsack(weights, values, capacity):
    n = len(values)
    ratio = [(values[i] / weights[i], weights[i], values[i]) for i in range(n)]
    ratio.sort(reverse=True)
    total_value = 0.0
    knapsack_items = []
    for r, w, v in ratio:
        if capacity == 0:
            break
        if w <= capacity:
            capacity -= w
            total_value += v
            knapsack_items.append((w, v, 1))  # 1 = full item taken
        else:
            # Take fraction of the item
            fraction = capacity / w
            total_value += v * fraction
            knapsack_items.append((w, v, fraction))
            capacity = 0
    return total_value, knapsack_items

values = [60, 100, 120]
weights = [10, 20, 30]
capacity = 50

max_value, items_taken = fractional_knapsack(weights, values, capacity)

print("Maximum Value in Knapsack:", max_value)
print("Items taken (weight, value, fraction):")
for item in items_taken:
    print(item)
