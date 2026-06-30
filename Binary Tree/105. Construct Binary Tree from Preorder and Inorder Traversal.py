# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if not preorder or not inorder:
            return None
        
        # Root is always the first element in preorder
        root_val = preorder[0]
        root = TreeNode(root_val) # type: ignore
        
        # Find root index in inorder
        idx = inorder.index(root_val)
        
        # Left subtree uses inorder[:idx]
        # Right subtree uses inorder[idx+1:]
        root.left = self.buildTree(preorder[1:1+idx], inorder[:idx])
        root.right = self.buildTree(preorder[1+idx:], inorder[idx+1:])
        
        return root
