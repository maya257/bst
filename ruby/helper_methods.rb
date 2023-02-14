module HelperMethods
  def insert_array(array)
    tree = BinarySearchTree.new
    array.each do |num|
      tree.add_to_search_tree(num)
    end
    return tree
  end
end



