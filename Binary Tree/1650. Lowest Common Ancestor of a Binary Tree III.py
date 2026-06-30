# Definition for a Node.
# class Node:
#     def __init__(self, val):
#         self.val = val
#         self.left = None
#         self.right = None
#         self.parent = None

class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node': # type: ignore
        # Use two pointers, similar to intersection of linked lists
        a, b = p, q
        while a != b:
            a = a.parent if a else q
            b = b.parent if b else p
        return a
