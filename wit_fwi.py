from read_data import read_data

database = read_data('./data/chess.dat.txt')


# Định nghĩa cấu trúc dữ liệu WIT-tree Node
class WITNode:
    def __init__(self):
        self.children = {}
        self.weight = 0
        self.itemsets = []

# Hàm thêm một tập hạng mục có trọng số vào WIT-tree
def insert_wit_tree(root, itemset, weight):
    node = root
    for item in itemset:
        if item not in node.children:
            node.children[item] = WITNode()
        node = node.children[item]
        node.itemsets.append(itemset)
        node.weight += weight

# Hàm khai thác các tập phổ biến có trọng số từ WIT-tree
def mine_frequent_weighted_itemsets_wit_tree(node, min_support, current_itemset, results):
    for item, child_node in node.children.items():
        new_itemset = current_itemset + [item]
        total_weight = sum(child_node.weight for itemset in child_node.itemsets)
        if total_weight >= min_support:
            results.append((new_itemset, total_weight))
            mine_frequent_weighted_itemsets_wit_tree(child_node, min_support, new_itemset, results)

# Hàm chính của thuật toán WIT-FWI sử dụng cây WIT-tree
def WIT_FWI(database, min_support):
    # Tạo nút gốc cho WIT-tree
    root = WITNode()

    # Xây dựng WIT-tree từ cơ sở dữ liệu có trọng số
    for itemset in database:
        insert_wit_tree(root, itemset, 1)  # Giả định trọng số của mỗi giao dịch là 1

    # Khai thác các tập phổ biến có trọng số từ WIT-tree
    frequent_weighted_itemsets = []
    mine_frequent_weighted_itemsets_wit_tree(root, min_support, [], frequent_weighted_itemsets)

    return frequent_weighted_itemsets

# Giá trị support tối thiểu
min_support = 75

# Gọi thuật toán WIT-FWI sử dụng cây WIT-tree và hiển thị kết quả
results = WIT_FWI(database, min_support)
print(results)
print("Frequent Weighted Itemsets:")
for itemset, weight in results:
    print(f"{itemset}: {weight}")