# Sample transaction data have weighted mark
transaction_data = [
    {'items': ['A', 'B'], 'weight': 2},
    {'items': ['A'], 'weight': 1},
    {'items': ['B', 'C'], 'weight': 3},
]

# Step 1: Generate Frequent Itemsets
min_support = 0.2

frequent_itemsets = {}
for transaction in transaction_data:
    for item in transaction['items']:
        if item in frequent_itemsets:
            frequent_itemsets[item] += transaction['weight']
        else:
            frequent_itemsets[item] = transaction['weight']

frequent_itemsets = {item: support for item, support in frequent_itemsets.items() if support >= min_support}

# Step 2: Generate Association Rules
association_rules = []
for itemset in frequent_itemsets:
    for item in frequent_itemsets:
        if item != itemset:
            # Calculate confidence and lift
            confidence = frequent_itemsets[itemset] / frequent_itemsets[item]
            lift = frequent_itemsets[itemset] / (frequent_itemsets[item] * frequent_itemsets[itemset])

            # Add rule to association_rules list
            association_rules.append({
                'itemset': itemset,
                'item': item,
                'confidence': confidence,
                'lift': lift
            })

# Step 3: Filtering Rules
min_confidence = 0.5
filtered_rules = [rule for rule in association_rules if rule['confidence'] >= min_confidence]

# Print the filtered rules
for rule in filtered_rules:
    print(f"Rule: {rule['itemset']} => {rule['item']}, Confidence: {rule['confidence']}, Lift: {rule['lift']}")
