# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def pathSum(self, root, target):
        """
        :type root: TreeNode
        :type target: int
        :rtype: int
        """
        prefix_count = {0: 1}  # base case: one way to have sum = 0

        def dfs(node, curr_sum):
            if not node:
                return 0
            
            curr_sum += node.val
            # Count paths ending at current node with sum = target
            res = prefix_count.get(curr_sum - target, 0)
            
            # Update prefix_count
            prefix_count[curr_sum] = prefix_count.get(curr_sum, 0) + 1
            
            # Explore children
            res += dfs(node.left, curr_sum)
            res += dfs(node.right, curr_sum)
            
            # Backtrack
            prefix_count[curr_sum] -= 1
            
            return res
        
        return dfs(root, 0)
