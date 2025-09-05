from collections import deque
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = {i:[] for i in range(numCourses)}

        in_d = [0]*numCourses
        out_d = [0]*numCourses
        for pre in prerequisites:
            graph[pre[1]].append(pre[0])
            out_d[pre[1]] += 1
            in_d[pre[0]] += 1

        q = deque()
        res = []
        visited = [False for i in range(numCourses)]
        flag = False
        for i in range(numCourses):
            if in_d[i] == 0:
                flag = True
                q.append(i)
                # res.append(i)
                visited[i] = True
            if out_d[i] == 0:
                flag = True
        if not flag:
            return []
        
        
        def bfs(q):
            next_q = deque()
            while(q):
                curr = q.popleft()
                res.append(curr)
                for j in graph[curr]:
                    visited[j] = True
                    in_d[j] -= 1
                    if in_d[j] == 0:
                        q.append(j)

        bfs(q)
        if len(res) != numCourses:
            return []
        return res
        
                

                
