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
            # base case 1
            if start > end:
                variations.append(None)
                return variations
            # base case 2
            if (start, end) in dp:
                return dp[(start, end)]
            for i in range(start, end + 1):
                print(f"For i={i}:")
                
                leftSubTrees = helper(start, i - 1)
                print(f"   Left Subtrees for {i}: {leftSubTrees}")
                
                rightSubTrees = helper(i + 1, end)
                print(f"   Right Subtrees for {i}: {rightSubTrees}")
                
                for left in leftSubTrees:
                    for right in rightSubTrees:
                        root = TreeNode(i)
                        root.left = left
                        root.right = right
                        variations.append(root)
            dp[(start, end)] = variations
            return variations
        
        
        return helper(1, n)
    
# Function to convert a tree to a list
def tree_to_list(root):
    if root is None:
        return []
    result = [root.val]
    left_list = tree_to_list(root.left)
    right_list = tree_to_list(root.right)
    result.extend(left_list)
    result.extend(right_list)
    return result

# Instantiate the Solution class
solution = Solution()

# Set the value of n
n = 3

# Generate all possible unique binary search trees with nodes containing values from 1 to n
output_trees = solution.generateTrees(n)

# Convert each tree to a list and concatenate them into a single list
all_trees_list = [tree_to_list(tree) for tree in output_trees]

# Print the single list containing all tree values
print(all_trees_list)