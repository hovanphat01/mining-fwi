from itertools import combinations
from collections import defaultdict

def generate_frequent_itemsets(transactions, min_weighted_support):
    """
    Generate frequent itemsets from a list of transactions based on weighted support.
    Tạo ra tập phổ biến từ một list các giao dịch dựa trên hỗ trợ có trọng số
    
    Parameters:
        transactions (list of dicts): Một list các giao dịch, trong đó mỗi giao dịch là một dictionary
                                     với các mục như các key và trọng số tương ứng như giá trị
        min_weighted_support (int): Ngưỡng trọng số hỗ trợ tối thiểu.
        
    Returns:
        In ra tập phổ biến có trọng số.
    """


    # Calculate the weighted support for each item
    item_weight = defaultdict(int)
    for transaction in transactions:
        for item, weight in transaction.items():
            item_weight[item] += weight

    # Generate frequent itemsets:
    frequent_itemsets = []
    for length in range(1, len(item_weight) + 1):
        for items in combinations(item_weight.keys(), length):
            total_weight = sum(item_weight[item] for item in items)
            if total_weight >= min_weighted_support:
                frequent_itemsets.append((items, total_weight))
    
    # for items, total_weight in frequent_itemsets:
    #     print(f"Itemset: {', '.join(items)} | Total Weight: {total_weight}")

# # Minimum weighted support threshold
# min_weighted_support =2
# database = [
#     {'Beer': 3, 'Sausage': 2, 'Egg': 1},
#     {'Beer': 1, 'Durian': 2, 'Yaourt': 2},
#     {'Beer': 2, 'Durian': 3, 'Yaourt': 2, 'Beef': 1},
#     {'Durian': 1, 'Yaourt': 2, 'Beef': 2}
# ]

# frequent_itemsets = generate_frequent_itemsets(database, min_weighted_support)
