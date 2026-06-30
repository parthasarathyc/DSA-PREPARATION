from collections import defaultdict, deque

class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        graph = defaultdict(list)
        indegree = [0] * numCourses
        
        # Build graph and indegree array
        for dest, src in prerequisites:
            graph[src].append(dest)
            indegree[dest] += 1
        
        # Initialize queue with courses having no prerequisites
        queue = deque([i for i in range(numCourses) if indegree[i] == 0])
        order = []
        
        while queue:
            course = queue.popleft()
            order.append(course)
            for nei in graph[course]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    queue.append(nei)
        
        # If we scheduled all courses, return order
        if len(order) == numCourses:
            return order
        else:
            return []
