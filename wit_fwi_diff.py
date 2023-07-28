from read_data import read_data

database = read_data('./data/chess.dat.txt')

# Định nghĩa cấu trúc dữ liệu WIT-tree Node
class WITNode:
    def __init__(self):
        self.children = {}
        self.weight = 0
        self.itemsets = []

# Định nghĩa cấu trúc dữ liệu Diff-WIT-tree Node
class DiffWITNode:
    def __init__(self):
        self.children = {}
        self.weight = 0

# Hàm thêm một tập hạng mục vào WIT-tree
def insert_wit_tree(root, itemset):
    node = root
    for item in itemset:
        if item not in node.children:
            node.children[item] = WITNode()
        node = node.children[item]
        node.itemsets.append(itemset)
        node.weight += 1

# Hàm thêm một tập hạng mục vào Diff-WIT-tree
def insert_diff_wit_tree(root, itemset):
    node = root
    for item in itemset:
        if item not in node.children:
            node.children[item] = DiffWITNode()
        node = node.children[item]
        node.weight += 1

# Hàm khai thác các tập phổ biến từ WIT-tree
def mine_frequent_itemsets_wit_tree(node, min_support, current_itemset, results):
    for item, child_node in node.children.items():
        new_itemset = current_itemset + (item,)
        total_weight = len(child_node.itemsets)
        if total_weight >= min_support:
            results.append((new_itemset, total_weight))
            mine_frequent_itemsets_wit_tree(child_node, min_support, new_itemset, results)

# Hàm khai thác các tập phổ biến từ Diff-WIT-tree
def mine_frequent_itemsets_diff_wit_tree(node, min_support, current_itemset, results):
    for item, child_node in node.children.items():
        new_itemset = current_itemset + (item,)
        if child_node.weight >= min_support:
            results.append((new_itemset, child_node.weight))
            mine_frequent_itemsets_diff_wit_tree(child_node, min_support, new_itemset, results)

# Hàm chính của thuật toán WIT-FWI-DIFF
def WIT_FWI_DIFF(database, min_support):
    # Tạo nút gốc cho WIT-tree và Diff-WIT-tree
    wit_root = WITNode()
    diff_root = DiffWITNode()

    # Xây dựng WIT-tree và Diff-WIT-tree từ cơ sở dữ liệu
    for itemset in database:
        insert_wit_tree(wit_root, itemset)
        insert_diff_wit_tree(diff_root, itemset)

    # Khai thác các tập phổ biến từ WIT-tree
    frequent_itemsets = []
    mine_frequent_itemsets_wit_tree(wit_root, min_support, (), frequent_itemsets)

    # Khai thác các tập phổ biến từ Diff-WIT-tree
    frequent_itemsets_diff = []
    mine_frequent_itemsets_diff_wit_tree(diff_root, min_support, (), frequent_itemsets_diff)

    # So sánh kết quả của hai phương pháp và chỉ giữ lại các itemset phổ biến chung
    common_itemsets = set(frequent_itemsets) & set(frequent_itemsets_diff)

    return list(common_itemsets)



# Giá trị support tối thiểu
min_support = 75

# Gọi thuật toán WIT-FWI-DIFF và hiển thị kết quả
results = WIT_FWI_DIFF(database, min_support)
print("Common Frequent Itemsets:")
for itemset, support in results:
    print(f"{itemset}: {support}")
