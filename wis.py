from itertools import combinations
from collections import defaultdict

# Sample transactions with items and their weights
transactions = [
    {'A': 3, 'B': 2, 'C': 1},
    {'A': 1, 'B': 2, 'D': 2},
    {'A': 2, 'B': 3, 'C': 2, 'E': 1},
    {'B': 1, 'C': 2, 'E': 2}
]

# Minimum weighted support threshold
min_weighted_support = 5

# Calculate the weighted support for each item
item_weight = defaultdict(int)
for transaction in transactions:
    for item, weight in transaction.items():
        item_weight[item] += weight

# Generate frequent itemsets
frequent_itemsets = []
for length in range(1, len(item_weight) + 1):
    for items in combinations(item_weight.keys(), length):
        total_weight = sum(item_weight[item] for item in items)
        if total_weight >= min_weighted_support:
            frequent_itemsets.append((items, total_weight))

# Display the frequent itemsets
for items, total_weight in frequent_itemsets:
    print(f"Itemset: {', '.join(items)} | Total Weight: {total_weight}")
