import sys



class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right  = None

class BiTree:
    def __init__(self):
        self.root = None


    def is_bst(self, root):

        maxx = sys.maxsize
        minn = -sys.maxsize - 1

        return self.is_node_value_valid(root, minn, maxx)

    def is_node_value_valid(self, node, minn, maxx):
        if node == None:
            return True
        elif node.value <= minn or node.value >= maxx:
            return False

        return (self.is_node_value_valid(node.left, minn, node.value) and
                self.is_node_value_valid(node.right, node.value, maxx)
                )



root = Node(2)
root.left = Node(1)
root.right = Node(4)
# root.left.left = Node(3)
# root.left.right = Node(4)
root.right.left = Node(3)
root.right.right = Node(5)
new_tree = BiTree()
print(new_tree.is_bst(root))