# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        
        # Compute left and right depths
        def get_depth(node):
            depth = 0
            while node:
                depth += 1
                node = node.left
            return depth
        
        left_depth = get_depth(root.left)
        right_depth = get_depth(root.right)
        
        if left_depth == right_depth:
            # Left subtree is perfect
            return (1 << left_depth) + self.countNodes(root.right)
        else:
            # Right subtree is perfect
            return (1 << right_depth) + self.countNodes(root.left)
