from collections import deque
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = {i:[] for i in range(numCourses)}
        visited = [False]*numCourses
        in_d = [0]*numCourses
        q = deque()
        res = 0
        for pre in prerequisites:
            graph[pre[1]].append(pre[0])
            in_d[pre[0]] += 1
        
        print(in_d)
        flag = True
        for i in range(numCourses):
            if in_d[i] == 0:
                q.append(i)
                flag = False
                res += 1    

        if not len(prerequisites):
            return True
        if flag:
            return False

        print(res)
        

        def bfs(res):
            # res = 0
            while(q):
                curr = q.popleft()
                visited[curr] = True
                for j in graph[curr]:
                    in_d[j] -= 1
                    if in_d[j] == 0:
                        res += 1
                        q.append(j)
                
            if not q and res != numCourses:
                return False
            return True
        
        val = bfs(res)

        return val




