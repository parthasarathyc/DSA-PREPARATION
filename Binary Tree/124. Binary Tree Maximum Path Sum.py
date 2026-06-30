# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxPathSum(self, root):
        self.max_sum = float('-inf')
        
        def dfs(node):
            if not node:
                return 0
            
            # Compute max path sum from left and right subtrees
            left = max(dfs(node.left), 0)   # ignore negative paths
            right = max(dfs(node.right), 0)
            
            # Update global max with path through current node
            self.max_sum = max(self.max_sum, node.val + left + right)
            
            # Return max path sum including current node (one side only)
            return node.val + max(left, right)
        
        dfs(root)
        return self.max_sum
# Tree:   -10
#         /  \
#        9   20
#           /  \
#          15   7

root = TreeNode(-10) # type: ignore
root.left = TreeNode(9) # type: ignore
root.right = TreeNode(20) # type: ignore
root.right.left = TreeNode(15) # type: ignore
root.right.right = TreeNode(7) # type: ignore

print(Solution().maxPathSum(root))  # Output: 42
 