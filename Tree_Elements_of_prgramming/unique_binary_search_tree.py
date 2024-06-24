class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def generateTrees(self, n):
        dp = {}
        
        def helper(start, end):
            variations = []
            if start > end:
                variations.append(None)
                return variations
            if (start, end) in dp:
                return dp[(start, end)]
            
            for i in range(start, end + 1):
                print(f"For i={i}:")
                
                leftSubTrees = helper(start, i - 1)
                print(f"   Left Subtrees for {i}: {[node.val if node else None for node in leftSubTrees]}")
                
                rightSubTrees = helper(i + 1, end)
                print(f"   Right Subtrees for {i}: {[node.val if node else None for node in rightSubTrees]}")
                
                for left in leftSubTrees:
                    for right in rightSubTrees:
                        root = TreeNode(i)
                        root.left = left
                        root.right = right
                        variations.append(root)
                print(f"   Variations for {i}: {[node.val if node else None for node in variations]}")
                print(f"   Tree structure for {i}:")
                for tree in variations:
                    self.print_tree(tree)
                    print()
                
            dp[(start, end)] = variations
            return variations
        
        return helper(1, n)
    def print_tree(self, root, level=0):
        if root is None:
            return
        self.print_tree(root.right, level + 1)
        print("    " * level + str(root.val))
        self.print_tree(root.left, level + 1)
        
        

# Instantiate the Solution class
solution = Solution()

# Set the value of n
n = 4

# Generate all possible unique binary search trees with nodes containing values from 1 to n
output_trees = solution.generateTrees(n)
