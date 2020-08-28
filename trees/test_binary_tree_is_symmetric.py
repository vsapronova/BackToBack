class Node:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None



    def is_symmetric(self, root):
        if root == None:
            return True

        return self.check_symmetry(root.left, root.right)

    def check_symmetry(self, left_subtree_root, right_subtree_root):
        if (left_subtree_root == None and right_subtree_root == None):
            return True

        if (left_subtree_root != None and right_subtree_root != None):
            return (
                left_subtree_root.value == right_subtree_root.value and
                self.check_symmetry(left_subtree_root.right, right_subtree_root.left) and
                self.check_symmetry(left_subtree_root.left,
                                    right_subtree_root.right)
            )

        return False
root = Node(1)
root.left = Node(2)
root.right = Node(2)
root.left.left = Node(3)
root.left.right = Node(4)
root.right.left = Node(4)
root.right.right = Node(3)
new_tree = BinaryTree()
print(new_tree.is_symmetric(root))