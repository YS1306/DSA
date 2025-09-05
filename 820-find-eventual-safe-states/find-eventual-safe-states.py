from collections import deque
class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        inv_graph = [[] for i in range(n)]
        in_d = [0]*n
        q = deque()
        res = []
        for i in range(n):
            for j in graph[i]:
                in_d[i] += 1
                inv_graph[j].append(i)

        for i in range(n-1,-1,-1):
            if in_d[i] == 0:
                q.append(i)
                res.append(i)

        while(q):
            curr = q.popleft()
            for j in reversed(inv_graph[curr]):
                in_d[j] -= 1
                if in_d[j] == 0:
                    q.append(j)
                    res.append(j)
                
        
        return sorted(res)
