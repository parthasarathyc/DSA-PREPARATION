"""LeetCode 138. Copy List with Random Pointer (Python)
Approach: Hash Map (Optimal)

Idea:

Create a copy of each node and store the mapping:
Original Node → Copied Node
In a second pass, connect the next and random pointers of the copied nodes.

Time Complexity: O(n)
Space Complexity: O(n)

Python Solution"""
class Solution:
    def copyRandomList(self, head):
        if not head:
            return None

        # Map original node -> copied node
        old_to_new = {}

        # Create copy of each node
        curr = head
        while curr:
            old_to_new[curr] = Node(curr.val) # type: ignore
            curr = curr.next

        # Assign next and random pointers
        curr = head
        while curr:
            old_to_new[curr].next = old_to_new.get(curr.next)
            old_to_new[curr].random = old_to_new.get(curr.random)
            curr = curr.next

        return old_to_new[head]