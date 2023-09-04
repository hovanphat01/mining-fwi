# Định nghĩa cấu trúc dữ liệu WIT-tree Node
class WITNode:
    """
        Khởi tạo nút cây WTI

        Attributes:
            children (dict): một dictionary của nút cây con.
            weight (int): Tích lũy trọng số của các giao dịch trong node.
            itemsets (list): Một list của các tập mục có liên quan với node.
    """
    def __init__(self):
        self.children = {}
        self.weight = 0
        self.itemsets = []

# Hàm thêm một tập hạng mục có trọng số vào WIT-tree
def insert_wit_tree(root, itemset, weight):
    """
    Thêm trọng số tập mục vào WIT-tree.

    Args:
        root (WITNode): Node gốc của WIT-tree.
        itemset (list): Tập mục được thêm vào.
        weight (int): Trọng số của tập mục.

    Returns:
        None
    """
    node = root
    for item in itemset:
        if item not in node.children:
            node.children[item] = WITNode()
        node = node.children[item]
        node.itemsets.append(itemset)
        node.weight += weight

# Hàm khai thác các tập phổ biến có trọng số từ WIT-tree
def mine_frequent_weighted_itemsets_wit_tree(node, min_support, current_itemset, results):
    """
    Đệ quy khai thác các tập phổ biến có trọng số từ WIT-tree
    
    Args:
        node (WITNode): Node hiện tại đang được xử lý.
        min_support (int): Ngưỡng hỗ trợ nhỏ nhất.
        current_itemset (list): Tập mục hiện tại đang được xây dựng.
        results (list): List chứa các tập phổ biến có trọng số.

    Returns:
        None
    """
    for item, child_node in node.children.items():
        new_itemset = current_itemset + [item]
        total_weight = sum(child_node.weight for itemset in child_node.itemsets)
        if total_weight >= min_support:
            results.append((new_itemset, total_weight))
            mine_frequent_weighted_itemsets_wit_tree(child_node, min_support, new_itemset, results)

# Hàm chính của thuật toán WIT-FWI sử dụng cây WIT-tree
def WIT_FWI(database, min_support):
    """
    Thực thi thuật toán WIT-FWI sử dụng WIT-tree.

    Args:
        database (list): List các giao dịch có trọng số .
        min_support (int): Ngưỡng hỗ trợ nhỏ nhất.

    Returns:
        list: Một list dạng tuples chứa các tập phổ biến có trọng số và tổng trọng số của chúng.

    """
    # Tạo nút gốc cho WIT-tree
    root = WITNode()

    # Xây dựng WIT-tree từ cơ sở dữ liệu có trọng số
    for itemset in database:
        insert_wit_tree(root, itemset, 1)  # Giả định trọng số của mỗi giao dịch là 1

    # Khai thác các tập phổ biến có trọng số từ WIT-tree
    frequent_weighted_itemsets = []
    mine_frequent_weighted_itemsets_wit_tree(root, min_support, [], frequent_weighted_itemsets)

    return frequent_weighted_itemsets

# from read_data import read_data, transform_to_data
# from sklearn.model_selection import train_test_split
# data = read_data('./data/chess.dat.txt')
# database = transform_to_data(data)
# train_data, test_data = train_test_split(database, test_size=0.2)
# # # Giá trị support tối thiểu
# min_support = 150
# # database = [
# #     {'Beer': 3, 'Sausage': 2, 'Egg': 1},
# #     {'Beer': 1, 'Durian': 2, 'Yaourt': 2},
# #     {'Beer': 2, 'Durian': 3, 'Yaourt': 2, 'Beef': 1},
# #     {'Durian': 1, 'Yaourt': 2, 'Beef': 2}
# # ]
# # Gọi thuật toán WIT-FWI sử dụng cây WIT-tree và hiển thị kết quả
# results = WIT_FWI(test_data, min_support)
# print("Frequent Weighted Itemsets:")
# for itemset, weight in results:
#     print(f"Itemset: {', '.join(itemset)} | Total Weight: {weight}")