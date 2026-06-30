'''LeetCode 148. Sort List (Python)
Approach: Merge Sort on Linked List (Optimal)

Idea:

Use Merge Sort because linked lists do not support random access efficiently.
Find the middle of the list using slow and fast pointers.
Recursively sort the left and right halves.
Merge the two sorted halves.

Time Complexity: O(n log n)
Space Complexity: O(log n) (recursive stack)

Python Solution'''
class Solution:
    def sortList(self, head):
        if not head or not head.next:
            return head

        # Find middle
        slow = head
        fast = head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        mid = slow.next
        slow.next = None

        # Sort left and right halves
        left = self.sortList(head)
        right = self.sortList(mid)

        # Merge
        return self.merge(left, right)

    def merge(self, l1, l2):
        dummy = ListNode(0) # type: ignore
        curr = dummy

        while l1 and l2:
            if l1.val < l2.val:
                curr.next = l1
                l1 = l1.next
            else:
                curr.next = l2
                l2 = l2.next
            curr = curr.next

        if l1:
            curr.next = l1
        else:
            curr.next = l2

        return dummy.next
'''Example

Input

head = [4,2,1,3]

Output

[1,2,3,4]
Another Example

Input

head = [-1,5,3,4,0]

Output

[-1,0,3,4,5]
Dry Run
Input
4 → 2 → 1 → 3

Split:

Left  : 4 → 2
Right : 1 → 3

Sort each half:

2 → 4

1 → 3

Merge:

1 → 2 → 3 → 4
Interview Explanation
Find the middle of the linked list using slow and fast pointers.
Split the list into two halves.
Recursively sort both halves.
Merge the two sorted linked lists.
Return the merged list.
Driver Code (for Local Testing)
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def createList(arr):
    dummy = ListNode()
    curr = dummy
    for x in arr:
        curr.next = ListNode(x)
        curr = curr.next
    return dummy.next

def printList(head):
    while head:
        print(head.val, end=" ")
        head = head.next

head = createList([4, 2, 1, 3])

sol = Solution()
result = sol.sortList(head)
printList(result)
Sample Output
1 2 3 4

This is the optimal O(n log n) solution using Merge Sort, which is the standard interview solution for LeetCode 148 – Sort List.'''