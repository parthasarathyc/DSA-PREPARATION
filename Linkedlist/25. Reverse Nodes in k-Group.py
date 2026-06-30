'''LeetCode 25. Reverse Nodes in k-Group (Python)
Approach: Iterative Linked List Reversal

Idea:

Count k nodes.
If fewer than k nodes remain, leave them unchanged.
Reverse exactly k nodes.
Connect the reversed group to the previous group.
Repeat until the end of the list.

Time Complexity: O(n)
Space Complexity: O(1)

Python Solution'''
class Solution:
    def reverseKGroup(self, head, k):
        dummy = ListNode(0) # type: ignore
        dummy.next = head
        groupPrev = dummy

        while True:
            kth = groupPrev

            # Find the kth node
            for _ in range(k):
                kth = kth.next
                if not kth:
                    return dummy.next

            groupNext = kth.next

            # Reverse the group
            prev = groupNext
            curr = groupPrev.next

            while curr != groupNext:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp

            temp = groupPrev.next
            groupPrev.next = kth
            groupPrev = temp
'''Example

Input

head = [1,2,3,4,5]
k = 2

Output

[2,1,4,3,5]
Another Example

Input

head = [1,2,3,4,5]
k = 3

Output

[3,2,1,4,5]
Dry Run
Input
1 → 2 → 3 → 4 → 5
k = 2

Reverse first group:

2 → 1 → 3 → 4 → 5'''