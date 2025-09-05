from collections import deque
class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        m = len(graph)
        visited = [0 for i in range(m)]
        globq1 = set()
        globq2 = set()

        def bfs(i,q1,q2):
            q1.append(i)
            visited[i] = 1
            flag = True
            while(q1 or q2):
                if flag:
                    curr = q1.popleft()
                    for j in graph[curr]:
                        if j in q1:
                            return False
                        elif not visited[j]:
                            q2.append(j)
                            visited[j] = 1
                    if not q1:
                        flag = False
                        q1 = deque()
                        continue
                    
                if not flag:
                    curr = q2.popleft()
                    for j in graph[curr]:
                        if j in q2:
                            return False
                        elif not visited[j]:
                            q1.append(j)
                            visited[j] = 1
                    if not q2:
                        flag = True
                        q2 = deque()
                        continue
            
            return True

        for i in range(m):
            q1 = deque()
            q2 = deque()
            if not visited[i]:
                val = bfs(i,q1,q2)
            if not val:
                return False
        
        return True