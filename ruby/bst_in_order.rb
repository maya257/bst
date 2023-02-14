require_relative 'Node'
require_relative 'Tree'
require_relative 'helper_methods'
include HelperMethods


def in_order(node, result = [])
  return if node.nil?
  in_order(node.left, result)
  result << node.data
  in_order(node.right, result)
  result
end

def binary_search_tree(array)
  tree = insert_array(array)
  in_order(tree.root).join(" ")
end





puts binary_search_tree([8, 3, 10, 1, 6, 14, 4, 7, 13])
# => "8 3 1 6 4 7 10 14 13"
