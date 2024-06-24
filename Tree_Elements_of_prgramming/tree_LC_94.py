# Definition for a binary tree node.
#  https://leetcode.com/problems/binary-tree-inorder-traversal/ solution
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def inorder_traversal(root):
    final_list = []
    def inorder(r):
        if not r :
            return

        inorder(r.left)
        final_list.append(r.val)
        inorder(r.right)
    inorder(root)
    return final_list
        

   
root = TreeNode(1)
root.left = TreeNode(None)
root.right = TreeNode(2)
root.right.left = TreeNode(3)

print(inorder_traversal(root))