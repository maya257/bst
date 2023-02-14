class BinarySearchTree
  attr_accessor :root
  def initialize(data = nil)
    @root = Node.new(data)
  end

  def add_to_search_tree(node = @root, data)
    return @root = Node.new(data) if node.data.nil?
    if data < node.data
      return node.left = Node.new(data) if node.left.nil?
      return add_to_search_tree(node.left, data) if node.left != nil?
    elsif data > node.data
      return node.right = Node.new(data) if node.right.nil?
      return add_to_search_tree(node.right, data) if !node.right.nil?
    end
    nil
  end

end
