from collections import deque
class Solution:
    
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m = len(mat)
        n = len(mat[0])
        nearest = [[-1 for j in range(n)] for i in range(m)]
        visited = []

        curr_q = deque()
        next_q = deque()
        visited = [[0 for j in range(n)] for i in range(m)]
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    nearest[i][j] = 0
                    visited[i][j] = 1
                    curr_q.append((i,j))


        
        while(curr_q or next_q):
            curr = curr_q.popleft()
            i,j = curr
            if j < n-1 and not visited[i][j+1] and mat[i][j+1] == 1:
                next_q.append((i,j+1))
                mat[i][j+1] = 0
                visited[i][j+1] = 1
                nearest[i][j+1]  = nearest[i][j]+1
            if j > 0 and not visited[i][j-1] and mat[i][j-1] == 1:
                next_q.append((i,j-1))
                mat[i][j-1] = 0
                visited[i][j-1] = 1
                nearest[i][j-1] = nearest[i][j]+1
            if i < m-1 and not visited[i+1][j] and mat[i+1][j] == 1:
                next_q.append((i+1,j))
                mat[i+1][j] = 0
                visited[i+1][j] = 1
                nearest[i+1][j] = nearest[i][j]+1
            if i > 0 and not visited[i-1][j] and mat[i-1][j] == 1:
                next_q.append((i-1,j))
                mat[i-1][j] = 0
                visited[i-1][j] = 1
                nearest[i-1][j] = nearest[i][j]+1
            
            if not curr_q:
                curr_q = next_q.copy()
                next_q = deque()

        

        return nearest