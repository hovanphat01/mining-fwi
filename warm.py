# # Sample transaction data have weighted mark
# # transaction_data = [
# #     {'items': ['A', 'B'], 'weight': 2},
# #     {'items': ['A'], 'weight': 1},
# #     {'items': ['B', 'C'], 'weight': 3},
# # ]

# transaction_data = [
#     {'Beer': 3, 'Sausage': 2, 'Egg': 1},
#     {'Beer': 1, 'Durian': 2, 'Yaourt': 2},
#     {'Beer': 2, 'Durian': 3, 'Yaourt': 2, 'Beef': 1},
#     {'Durian': 1, 'Yaourt': 2, 'Beef': 2}
# ]

# # Step 1: Generate Frequent Itemsets
# # min_support = 0.2
# min_support = 1

# frequent_itemsets = {}
# for transaction in transaction_data:
#     for item in transaction['items']:
#         if item in frequent_itemsets:
#             frequent_itemsets[item] += transaction['weight']
#         else:
#             frequent_itemsets[item] = transaction['weight']

# frequent_itemsets = {item: support for item, support in frequent_itemsets.items() if support >= min_support}

# # Step 2: Generate Association Rules
# association_rules = []
# for itemset in frequent_itemsets:
#     for item in frequent_itemsets:
#         if item != itemset:
#             # Calculate confidence and lift
#             confidence = frequent_itemsets[itemset] / frequent_itemsets[item]
#             lift = frequent_itemsets[itemset] / (frequent_itemsets[item] * frequent_itemsets[itemset])

#             # Add rule to association_rules list
#             association_rules.append({
#                 'itemset': itemset,
#                 'item': item,
#                 'confidence': confidence,
#                 'lift': lift
#             })

# # Step 3: Filtering Rules
# min_confidence = 0.5
# filtered_rules = [rule for rule in association_rules if rule['confidence'] >= min_confidence]

# # Print the filtered rules
# for rule in filtered_rules:
#     print(f"Rule: {rule['itemset']} => {rule['item']}, Confidence: {rule['confidence']}, Lift: {rule['lift']}")

from itertools import combinations
from collections import defaultdict

def generate_association_rules(transaction_data, min_support, min_confidence):
    """
    Tạo quy tắc kết hợp dựa trên dữ liệu giao dịch, hỗ trợ tối thiểu và độ tin cậy tối thiểu.
    
    Parameters:
        transaction_data (list of dicts): Một danh sách các giao dịch, trong đó mỗi giao dịch là 
                                          một từ điển với các mục là khóa và số lượng tương ứng là giá trị.
        min_support (int): Ngưỡng hỗ trợ tối thiểu cho tập phổ biến.
        min_confidence (float): Ngưỡng tin cậy tối thiểu cho các luật kết hợp.
        
    Returns:
        Danh sách các luật kết hợp thỏa mãn tiêu chí độ hỗ trợ và độ tin cậy đã cho.
    """
    # Calculate support for each item
    item_support = defaultdict(int)
    for transaction in transaction_data:
        for item_name, item_quantity in transaction.items():
            item_support[item_name] += item_quantity
    
    # Filter items based on minimum support
    frequent_items = {item: support for item, support in item_support.items() if support >= min_support}
    
    # Generate association rules
    association_rules = []
    for transaction in transaction_data:
        for item_name, item_quantity in transaction.items():
            for other_item in frequent_items:
                if item_name != other_item:
                    item_support_count = item_support[item_name]
                    other_item_support_count = item_support[other_item]
                    confidence = item_support_count / other_item_support_count
                    lift = confidence / (item_support[other_item] / len(transaction_data))
                    total_weight = item_quantity + item_support[other_item]
                    association_rules.append({
                        'itemset': {item_name},
                        'item': {other_item},
                        'confidence': confidence,
                        'lift': lift,
                        'total_weight': total_weight
                    })

    filtered_rules = [rule for rule in association_rules if rule['confidence'] >= min_confidence]
    return filtered_rules

# # Sample transaction data
# transaction_data = [
#     {'Beer': 3, 'Sausage': 2, 'Egg': 1},
#     {'Beer': 1, 'Durian': 2, 'Yaourt': 2},
#     {'Beer': 2, 'Durian': 3, 'Yaourt': 2, 'Beef': 1},
#     {'Durian': 1, 'Yaourt': 2, 'Beef': 2}
# ]

# min_support = 0.5
# min_confidence = 0.5

# filtered_rules = generate_association_rules(transaction_data, min_support, min_confidence)

# for rule in filtered_rules:
#     itemset = ', '.join(rule['itemset'])
#     item = ', '.join(rule['item'])
#     print(f"Itemset: {itemset} => {item}, Confidence: {rule['confidence']}, Lift: {rule['lift']}, Total Weight: {rule['total_weight']}")