require_relative 'Node'
require_relative 'Tree'
require_relative 'helper_methods'
include HelperMethods

def pre_order(node)
  if node == nil
    return ''
  end
  result = "#{node.data} "
  result += pre_order(node.left)
  result += pre_order(node.right)
end


def binary_search_tree(array)
  tree = insert_array(array) # in helper methods
  pre_order(tree.root).strip
end


puts binary_search_tree([8, 3, 10, 1, 6, 14, 4, 7, 13])
# => "1, 3, 4, 6, 7, 8, 10, 13, 14"
