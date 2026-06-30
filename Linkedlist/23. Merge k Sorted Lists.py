'''LeetCode 23. Merge k Sorted Lists (Python)
Approach: Min Heap (Priority Queue)

Idea:

Insert the first node of each linked list into a min heap.
Always remove the smallest node from the heap.
Add its next node (if it exists) into the heap.
Continue until the heap becomes empty.

Time Complexity: O(N log k)

N = Total number of nodes
k = Number of linked lists

Space Complexity: O(k)

Python Solution'''
import heapq

class Solution:
    def mergeKLists(self, lists):
        heap = []

        # Add first node of each list
        for i, node in enumerate(lists):
            if node:
                heapq.heappush(heap, (node.val, i, node))

        dummy = ListNode(0) # type: ignore
        current = dummy

        while heap:
            value, i, node = heapq.heappop(heap)

            current.next = node
            current = current.next

            if node.next:
                heapq.heappush(heap, (node.next.val, i, node.next))

        return dummy.next
'''Example

Input

lists = [[1,4,5],[1,3,4],[2,6]]

Output

[1,1,2,3,4,4,5,6]
Dry Run
Initial Heap
(1,List1)
(1,List2)
(2,List3)

Process:

Pop 1 → Push 4
Pop 1 → Push 3
Pop 2 → Push 6
Pop 3 → Push 4
Pop 4 → Push 5
Pop 4
Pop 5
Pop 6

Result:

1 → 1 → 2 → 3 → 4 → 4 → 5 → 6
Interview Explanation
Insert the first node of every linked list into a min heap.
Extract the smallest node from the heap.
Append it to the answer list.
If the extracted node has a next node, insert it into the heap.
Repeat until the heap is empty.
Driver Code (for local testing)
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Helper function to create linked list
def create_list(arr):
    dummy = ListNode()
    cur = dummy
    for x in arr:
        cur.next = ListNode(x)
        cur = cur.next
    return dummy.next

# Helper function to print linked list
def print_list(head):
    while head:
        print(head.val, end=" ")
        head = head.next

lists = [
    create_list([1,4,5]),
    create_list([1,3,4]),
    create_list([2,6])
]

sol = Solution()
result = sol.mergeKLists(lists)
print_list(result)
Sample Output
1 1 2 3 4 4 5 6

This is the optimal O(N log k) solution using a Min Heap (Priority Queue), which is the expected approach in coding interviews and on LeetCode.'''