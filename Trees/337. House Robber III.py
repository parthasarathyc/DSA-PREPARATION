# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def dfs(node):
            if not node:
                return (0, 0)  # (rob_this, not_rob_this)
            
            left = dfs(node.left)
            right = dfs(node.right)
            
            # If we rob this node, we cannot rob its children
            rob_this = node.val + left[1] + right[1]
            
            # If we don't rob this node, we can choose to rob or not rob children
            not_rob_this = max(left) + max(right)
            
            return (rob_this, not_rob_this)
        
        return max(dfs(root))
