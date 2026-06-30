# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        self.first = None
        self.second = None
        self.prev = TreeNode(float('-inf')) # type: ignore
        
        def inorder(node):
            if not node:
                return
            inorder(node.left)
            
            # Detect violation
            if self.prev.val > node.val:
                if not self.first:
                    self.first = self.prev
                self.second = node
            self.prev = node
            
            inorder(node.right)
        
        inorder(root)
        
        # Swap values of the two misplaced nodes
        self.first.val, self.second.val = self.second.val, self.first.val
