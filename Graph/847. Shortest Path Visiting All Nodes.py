from collections import deque

class Solution(object):
    def shortestPathLength(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: int
        """
        n = len(graph)
        target = (1 << n) - 1  # all nodes visited
        
        # Initialize BFS queue with all nodes
        queue = deque()
        visited = set()
        for i in range(n):
            mask = 1 << i
            queue.append((i, mask, 0))  # (node, visited_mask, steps)
            visited.add((i, mask))
        
        while queue:
            node, mask, steps = queue.popleft()
            if mask == target:
                return steps
            for nei in graph[node]:
                new_mask = mask | (1 << nei)
                if (nei, new_mask) not in visited:
                    visited.add((nei, new_mask))
                    queue.append((nei, new_mask, steps + 1))
