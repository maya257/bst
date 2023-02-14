from tree import BinarySearchTree

def binary_search_tree_pre_order(array):
    tree = BinarySearchTree()
    for num in array:
        tree.add_to_search_tree(data=num)
    return ' '.join(map(str, tree.pre_order_traversal()))

def binary_search_tree_in_order(array):
    bst = BinarySearchTree()
    for num in array:
        bst.add_to_search_tree(data=num)
    return ' '.join(map(str, bst.in_order_traversal()))

print("Pre-order traversal:")
print(binary_search_tree_pre_order([8, 3, 10, 1, 6, 14, 4, 7, 13]))
# Output: "8 3 1 6 4 7 10 14 13"

print("In-order traversal:")
print(binary_search_tree_in_order([8, 3, 10, 1, 6, 14, 4, 7, 13]))
# Output: "1 3 4 6 7 8 10 13 14"
