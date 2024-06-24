class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

    #      3
    #    /   \
    #   9     20
    #         / \
    #        15  7

def height(root):
    if root is None:
        return -1
    print(height(root.left) , "--->",root.data, height(root.right), "--->",root.data)
    return 1+max(height(root.left) , height(root.right))

def is_balanced(root):
    if root is None:
        return True
    
    else:
        left_tree = height(root.left)
        print('left_tree', left_tree, 'Val: --> ', root.data)
        right_tree = height(root.right)
        print('right_tree', right_tree, 'Val: --> ', root.data)
        if abs(left_tree - right_tree) <= 1 and is_balanced(root.left) and is_balanced(root.right):
            return True
        return False


root = Node(3)
root.left = Node(9)
root.right = Node(20)
root.right.left = Node(15)
root.right.right = Node(7)

print(height(root))
# print(is_balanced(root))


