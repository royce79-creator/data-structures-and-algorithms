from code_challenges.tree_breadth_first.tree_breadth_first import breadth_first
from code_challenges.trees.trees import BinaryTree, Node

def test_breadth_first():
  node = Node(1)
  node.left = Node(2)
  node.right = Node(3)
  node.left.left = Node(4)
  node.left.right = Node(5)
  root = BinaryTree(node)
  assert breadth_first(root) == [1, 2, 3, 4, 5]
