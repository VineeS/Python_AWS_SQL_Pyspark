class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def tree_traversal(tree):
    if tree:
        # Preorder: Root -> Left -> Right
        print('Preorder: %d' % tree.data)
        tree_traversal(tree.left)

        # Inorder: Left -> Root -> Right
        print('Inorder: %d' % tree.data)
        tree_traversal(tree.right)

        # Postorder: Left -> Right -> Root
        print('Postorder: %d' % tree.data)





tree = Node(1)
tree.left = Node(2)
tree.right = Node(3)
tree.left.left = Node(4)
tree.left.right = Node(5)
tree.left.right.left = Node(6)
tree.right.left = Node(7)
tree.right.right = Node(8)
tree.right.right.right = Node(9)

print("inorder --> ", tree_traversal(tree))
