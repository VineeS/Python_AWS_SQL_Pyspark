class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

def display(tree):
    list_in_order = []
    if tree is None:
        return list_in_order
    
    if tree.left is not None:
        list_in_order.extend(display(tree.left))

    list_in_order.append(tree.data)

    if tree.right is not None:
        list_in_order.extend(display(tree.right))
    return list_in_order

tree = Node(1)
tree.left = Node(2)
tree.right = Node(3)
tree.left.left = Node(4)
tree.left.right = Node(5)
tree.left.right.left = Node(6)
tree.right.left = Node(7)
tree.right.right = Node(8)
tree.right.right.right = Node(9)