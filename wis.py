def calculate_total_weight(itemset, support_table):

    """
    Tính tổng trọng số của một tập mục dựa trên bảng hỗ trợ.

    Args:
        itemset (freezeset): Tập mục cần tính tổng trọng số.
        support_table (dict): Từ điển chứa trọng số mục.

    Return:
        int: Tổng trọng số của itemet.
    """

    total_weight = 0
    for item in itemset:
        total_weight += support_table[item]
    return total_weight

def generate_candidate_itemsets(prev_itemsets):
    """
    Tạo các tập mục ứng viên bằng cách kết hợp các tập mục trước đó.

    Args:
        prev_itemsets (list): Danh sách các tập mục trước đó cùng với tổng trọng số của chúng.

    Return:
        list: Danh sách các tập mục ứng viên cùng với tổng trọng số của chúng.
    """
    candidate_itemsets = []
    for itemset1 in prev_itemsets:
        for itemset2 in prev_itemsets:
            new_itemset = itemset1[0].union(itemset2[0])
            total_weight = itemset1[1] + itemset2[1]
            if len(new_itemset) == len(itemset1[0]) + 1 and (new_itemset, total_weight) not in candidate_itemsets:
                candidate_itemsets.append((new_itemset, total_weight))
    return candidate_itemsets

def wis_algorithm(data, min_weight_threshold):
    """
    Chạy thuật toán Hỗ trợ tập mục có trọng số (WIS).

    Args:
        data (list): Danh sách các giao dịch, mỗi giao dịch chứa các mục có trọng số của chúng.
        min_weight_threshold (int): Tổng trọng số tối thiểu cho các tập mục thường xuyên.

    Return:
        list: Danh sách các tập mục thường xuyên cùng với tổng trọng số của chúng.
    """


    # Step 1: Xây dựng bảng hỗ trợ
    support_table = {}
    for transaction in data:
        for item, weight in transaction.items():
            if item in support_table:
                support_table[item] += weight
            else:
                support_table[item] = weight
    
    # Step 2: Khởi tạo các tập mục ứng viên
    candidate_itemsets = [({item}, support_table[item]) for item in support_table.keys()]
    
    # Step 3: Tạo các tập mục thường xuyên
    frequent_itemsets = []
    while candidate_itemsets:
        valid_candidates = []
        for candidate in candidate_itemsets:
            if candidate[1] >= min_weight_threshold:
                valid_candidates.append(candidate)
                frequent_itemsets.append(candidate)
        candidate_itemsets = generate_candidate_itemsets(valid_candidates)
    
    return frequent_itemsets
# from read_data import read_data, transform_to_data
# from sklearn.model_selection import train_test_split
# data = read_data('./data/chess.dat.txt')
# database = transform_to_data(data)
# train_data, test_data = train_test_split(database, test_size=0.05)

# min_weight_threshold =150
# frequent_itemsets = wis_algorithm(test_data, min_weight_threshold)

# print("Frequent Weighted Itemsets:")
# for itemset, total_weight in frequent_itemsets:
#     items = ", ".join(item for item in itemset)
#     print(f"Itemset: {items} | Total Weight: {total_weight}")
