# Binary Search Tree Implementations and Vizualizations
This is a project with implementations of a binary search tree data structure and it's traversal methods in Python, Ruby, and JavaScript.

## Getting Started
These instructions will help you set up and run the code in your local machine.

### Prequisites
- Python 3.x
- Ruby 3.x
- NodeJS 18.x

### Installing
Clone or download the repository to your local machine and then navigate to the project directory in your terminal.
```git clone https://github.com/mcrd25/bst.git``` <br>
```cd bst``` <br>

### Running the code
To run the code currently in the project repository, run the following commands in the terminal:

#### Python
`python3 main.py`<br>
The code takes in an array of integers and creates a binary search tree. It then outputs the pre-order and in-order traversal of the tree.

#### Ruby
`ruby bst_pre_order.rb `<br>
The code takes in an array of integers and creates a binary search tree. It then outputs the pre-order traversal of the tree.<br>
`ruby bst_in_order.rb `<br>
The code takes in an array of integers and creates a binary search tree. It then outputs the in-order traversal of the tree.

## Code Structure
### Python
The code is composed of two main classes: `Node` and `BinarySearchTree`. The Node class has two instance variables, `data` and `left` and `right`, which represent the value stored in the node and the left and right child nodes, respectively. The BinarySearchTree class has one instance variable, `root`, which represents the root node of the tree.

The `BinarySearchTree` class contains three methods: `add_to_search_tree`, `pre_order_traversal`, and `in_order_traversal`. The `add_to_search_tree` method takes in a node and data (most likely an integer in our exampls), and adds a new node to the binary search tree by following the binary search tree property. The `pre_order_traversal` method takes in a node and returns the pre-order traversal of the tree starting from that node and liekwise with the `in_order_traversal` method returning the in-order traversal of the tree.

The code also contains three functions: `binary_search_tree_pre_order`, `binary_search_tree_in_order` and `insert_array` (HelperMethods module). The binary_search_tree functions takes in an array of integers, creates a binary search tree using the insert_array function, and returns the pre-order and in-order traversal of the tree as a string. The insert_array function takes in an array of integers and returns a binary search tree created by inserting each element of the array into the tree.

### Ruby
Basically the same structure except the  pre-order traversals and in-order traversals are in their own scripts and not part of the `BinarySearchTree` class (Tree.rb). It's pretty straightforward.

## References


## Authors

👤 **Maya D. - child of God**

- GitHub: [@mcrd25](https://github.com/mcrd25)
- LinkedIn: [LinkedIn](https://linkedin.com/in/mayadouglas)

## 🤝 Contributing

Contributions, issues, and feature requests are welcome!

Feel free to check the [issues page](../../issues/).

## Show your support

Give a ⭐️ if you like this project!

## Acknowledgments


## 📝 License
