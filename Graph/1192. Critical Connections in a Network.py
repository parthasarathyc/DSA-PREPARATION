from collections import defaultdict

class Solution(object):
    def criticalConnections(self, n, connections):
        """
        :type n: int
        :type connections: List[List[int]]
        :rtype: List[List[int]]
        """
        graph = defaultdict(list)
        for u, v in connections:
            graph[u].append(v)
            graph[v].append(u)
        
        self.time = 0
        disc = [-1] * n
        low = [-1] * n
        res = []
        
        def dfs(u, parent):
            disc[u] = low[u] = self.time
            self.time += 1
            
            for v in graph[u]:
                if v == parent:
                    continue
                if disc[v] == -1:  # not visited
                    dfs(v, u)
                    low[u] = min(low[u], low[v])
                    if low[v] > disc[u]:
                        res.append([u, v])
                else:
                    low[u] = min(low[u], disc[v])
        
        dfs(0, -1)
        return res
