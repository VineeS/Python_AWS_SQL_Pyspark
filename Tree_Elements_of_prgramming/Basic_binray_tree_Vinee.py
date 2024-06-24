# DFS stands for Depth-First Search. It's an algorithm for traversing or searching tree or graph data structures.
#  In the context of trees, DFS starts at the root (or another arbitrarily selected node) and explores as 
# far as possible along each branch before backtracking.

# There are several variations of DFS, but they all follow the same basic principle:

# 1. **Depth-First Search (DFS)**: Visit the root node, then recursively visit the child nodes.
#  This process is continued until there are no more child nodes to visit.

# DFS can be further categorized into three types, based on the order in which nodes are visited:

# - **Preorder**: Visit the current node, then recursively visit the left and right subtrees.
# - **Inorder**: Recursively visit the left subtree, then visit the current node, then recursively visit the right subtree.
# - **Postorder**: Recursively visit the left and right subtrees, then visit the current node.

# These traversals have various applications in algorithms and data structures, such as searching, sorting, and expression evaluation.


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

def pre_order(tree):
    list_post_order = []
    if tree is None:
        return list_post_order
    
    list_post_order.append(tree.data)

    if tree.left is not None:
        list_post_order.extend(pre_order(tree.left))

    if tree.right is not None:
        list_post_order.extend(pre_order(tree.right))

    return list_post_order

def post_order(tree):
    list_post_order = []
    if tree is None:
        return 
    
    if tree.left is not None:
        list_post_order.extend(post_order(tree.left))

    if tree.right is not None:
        list_post_order.extend(post_order(tree.right))

    list_post_order.append(tree.data)

    return list_post_order

def depth_of_tree(tree):
    if tree is None:
        return 0
    else:
        depth_l_tree = depth_of_tree(tree.left)
        print('depth_l_tree', depth_l_tree, 'Val:', tree.data)
        depth_r_tree = depth_of_tree(tree.right)
        print('depth_r_tree', depth_r_tree, 'Val:', tree.data)

        if depth_l_tree > depth_r_tree:
            return 1 + depth_l_tree
        else:
            return 1 + depth_r_tree
    
        
def is_full_binary_tree(tree):
    if tree is None:
        return True
    if (tree.left is None) and (tree.right is None):
        return True
    if (tree.left is not None) and (tree.right is not None):
        return is_full_binary_tree(tree.left) and is_full_binary_tree(tree.right)
    else:
        return False
     

tree = Node(1)
tree.left = Node(2)
tree.right = Node(3)
tree.left.left = Node(4)
tree.left.right = Node(5)
tree.left.right.left = Node(6)
tree.right.left = Node(7)
tree.right.right = Node(8)
tree.right.right.right = Node(9)

print("inorder --> ", display(tree))
print("pre_order ---> ",pre_order(tree))
print("post_order ---> ",post_order(tree))
print("dept of tree --> ", depth_of_tree(tree))

    #      1
    #    /   \
    #   2     3
    #  / \     / \
    # 4   5  7   8
    #    /       \
    #   6         9


