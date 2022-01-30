class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

class BinaryTree:
    def __init__(self, root=None):
        self.root = root

    def pre_order(self):
        pre_list = []

        def walk(root):
            if root is None:
                return
            pre_list.append(root.value)
            walk(root.left)
            walk(root.right)

        walk(self.root)
        return pre_list

    def in_order(self):
        in_list = []

        def walk(root):
            if root is None:
                return

            walk(root.left)
            in_list.append(root.value)
            walk(root.right)

        walk(self.root)
        return in_list

    def post_order(self):
        post_list = []

        def walk(root):
            if root is None:
                return

            walk(root.left)
            walk(root.right)
            post_list.append(root.value)

        walk(self.root)
        return post_list

class BinarySearchTree(BinaryTree):

    def add(self, value):
        node = Node(value)
        if self.root is None:
            self.root = node

        def walk(root, add_node):
            if root is None:
                return

            if add_node.value < root.value:
                if root.left:
                    walk(root.left, add_node)
                else:
                    root.left = add_node
            else:
                if root.right:
                    walk(root.right, add_node)
                else:
                    root.right = add_node

        walk(self.root, node)

    def contains(self, value):
        if self.root is None:
            return False

        def walk(root, value):
            if root.value == value:
                return True
            elif value < root.value:
                if root.left:
                    return walk(root.left, value)
            elif value > root.value:
                if root.right:
                    return walk(root.right,value)
            return False

        return walk(self.root, value)
