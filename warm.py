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


# from read_data import read_data, transform_to_data
# from sklearn.model_selection import train_test_split
# data = read_data('./data/chess.dat.txt')
# database = transform_to_data(data)
# train_data, test_data = train_test_split(database, test_size=0.05)
# # Sample transaction data
# transaction_data = [
#     {'Beer': 3, 'Sausage': 2, 'Egg': 1},
#     {'Beer': 1, 'Durian': 2, 'Yaourt': 2},
#     {'Beer': 2, 'Durian': 3, 'Yaourt': 2, 'Beef': 1},
#     {'Durian': 1, 'Yaourt': 2, 'Beef': 2}
# ]

# min_support =150
# min_confidence = 1

# filtered_rules = generate_association_rules(test_data, min_support, min_confidence)

# for rule in filtered_rules:
#     itemset = ', '.join(rule['itemset'])
#     item = ', '.join(rule['item'])
#     print(f"Itemset: {itemset} => {item}, Confidence: {rule['confidence']}, Lift: {rule['lift']}, Total Weight: {rule['total_weight']}")