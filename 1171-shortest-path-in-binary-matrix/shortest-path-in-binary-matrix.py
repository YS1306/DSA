from collections import deque
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)
        q = deque()
        dist = [[10**7]*n for i in range(n)]
        if not grid[0][0]: 
            q.append((0,0,1))
            dist[0][0] = 1

        while(q):
            i,j,k = q.popleft()
            
            if i > 0 and j > 0 and not grid[i-1][j-1]:
                if dist[i-1][j-1] > k+1:
                    dist[i-1][j-1] = k+1
                    q.append((i-1, j-1, k+1)) 

            if i > 0 and not grid[i-1][j]:
                if dist[i-1][j] > k+1:
                    dist[i-1][j] = k+1
                    q.append((i-1,j,k+1))

            if i > 0 and j < n-1 and not grid[i-1][j+1]:
                if dist[i-1][j+1] > k+1:
                    dist[i-1][j+1] = k+1
                    q.append((i-1, j+1, k+1))
            
            if j < n-1 and not grid[i][j+1]:
                if dist[i][j+1] > k+1:
                    dist[i][j+1] = k+1
                    q.append((i, j+1, k+1))
                
            if i < n-1 and j < n-1 and not grid[i+1][j+1]:
                if dist[i+1][j+1] > k+1:
                    dist[i+1][j+1] = k+1
                    q.append((i+1, j+1,k+1))

            if i < n-1 and not grid[i+1][j]:
                if dist[i+1][j] > k+1:
                    dist[i+1][j] = k+1
                    q.append((i+1, j, k+1))

            if i < n-1 and j > 0 and not grid[i+1][j-1]:
                if dist[i+1][j-1] > k+1:
                    dist[i+1][j-1] = k+1
                    q.append((i+1, j-1, k+1))

            if j > 0 and not grid[i][j-1]:
                if dist[i][j-1] > k+1:
                    dist[i][j-1] = k+1
                    q.append((i, j-1, k+1))

        if dist[n-1][n-1] == 10**7:
            return -1

        else:
            return dist[n-1][n-1]
            
            

