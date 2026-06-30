'''LeetCode 460. LFU Cache (Python)
Approach: Hash Map + Frequency Lists (Optimal)

Idea:

Use:
A dictionary to store key → node.
A dictionary to store frequency → doubly linked list.
Every node stores:
key
value
frequency
When a key is accessed:
Increase its frequency.
Move it to the corresponding frequency list.
If the cache is full:
Remove the Least Frequently Used (LFU) node.
If there is a tie, remove the Least Recently Used (LRU) among them.

Time Complexity: O(1) for both get() and put().

Space Complexity: O(capacity)

Python Solution'''
from collections import defaultdict

class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.freq = 1
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def add(self, node):
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node

    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def pop_last(self):
        if self.head.next == self.tail:
            return None
        node = self.tail.prev
        self.remove(node)
        return node

    def is_empty(self):
        return self.head.next == self.tail


class LFUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.minFreq = 0
        self.nodes = {}
        self.freqMap = defaultdict(DoublyLinkedList)

    def update(self, node):
        freq = node.freq
        self.freqMap[freq].remove(node)

        if freq == self.minFreq and self.freqMap[freq].is_empty():
            self.minFreq += 1

        node.freq += 1
        self.freqMap[node.freq].add(node)

    def get(self, key: int) -> int:
        if key not in self.nodes:
            return -1

        node = self.nodes[key]
        self.update(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        if self.capacity == 0:
            return

        if key in self.nodes:
            node = self.nodes[key]
            node.value = value
            self.update(node)
            return

        if len(self.nodes) == self.capacity:
            node = self.freqMap[self.minFreq].pop_last()
            del self.nodes[node.key]

        newNode = Node(key, value)
        self.nodes[key] = newNode
        self.freqMap[1].add(newNode)
        self.minFreq = 1
"""Example

Input

LFUCache(2)

put(1,1)
put(2,2)
get(1)
put(3,3)
get(2)
get(3)
put(4,4)
get(1)
get(3)
get(4)
Output
null
null
null
1
null
-1
3
null
-1
3
4
Explanation
Cache Capacity = 2

put(1,1)
Cache = {1}

put(2,2)
Cache = {1,2}

get(1)
Frequency of key 1 becomes 2

put(3,3)

Cache Full

Least Frequently Used = key 2

Remove key 2

Insert key 3

Cache = {1,3}
Interview Explanation
Store each node in a hash map for O(1) lookup.
Maintain separate doubly linked lists for each frequency.
On get():
Increase the node's frequency.
Move it to the corresponding frequency list.
On put():
Update an existing key if present.
Otherwise, if the cache is full, remove the least frequently used node (and least recently used if tied).
Insert the new node with frequency 1.
Driver Code
cache = LFUCache(2)

cache.put(1, 1)
cache.put(2, 2)
print(cache.get(1))   # 1

cache.put(3, 3)
print(cache.get(2))   # -1
print(cache.get(3))   # 3

cache.put(4, 4)
print(cache.get(1))   # -1
print(cache.get(3))   # 3
print(cache.get(4))   # 4
Sample Output
1
-1
3
-1
3
4

This is the optimal O(1) solution for both get() and put(), which is the standard interview solution for LeetCode 460 – LFU Cache."""