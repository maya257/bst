from node import Node
class BinarySearchTree:
    def __init__(self, data=None):
        self.root = Node(data)

    def add_to_search_tree(self, node=None, data=None):
        if node is None:
            node = self.root
        if node.data is None:
            node.data = data
            return node
        if data < node.data:
            if node.left is None:
                node.left = Node(data)
                return node.left
            return self.add_to_search_tree(node.left, data)
        elif data > node.data:
            if node.right is None:
                node.right = Node(data)
                return node.right
            return self.add_to_search_tree(node.right, data)
        return None

    def in_order_traversal(self, node=None, result=[]):
        if node is None:
            node = self.root
        if node.left is not None:
            self.in_order_traversal(node.left, result)
        result.append(node.data)
        if node.right is not None:
            self.in_order_traversal(node.right, result)
        return result

    def pre_order_traversal(self, node=None, result=[]):
        if node is None:
            node = self.root
        result.append(node.data)
        if node.left is not None:
            self.pre_order_traversal(node.left, result)
        if node.right is not None:
            self.pre_order_traversal(node.right, result)
        return result
