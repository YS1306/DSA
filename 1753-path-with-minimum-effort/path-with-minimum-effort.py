from heapq import heappop, heappush, heapify

class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        Q = []
        m = len(heights)
        n = len(heights[0])
        dist = [[10**7]*n for i in range(m)]
        
        parent = [[(i,j) for j in range(n)] for i in range(m)]
        heappush(Q,(0,0,0))
        dist[0][0] = 0

        while(Q):
            d,i,j = heappop(Q)
            if j > 0 and dist[i][j-1] > d and dist[i][j-1] >  abs(heights[i][j]-heights[i][j-1]):
                dist[i][j-1] = max(d, abs(heights[i][j-1]-heights[i][j]))
                parent[i][j-1] = (i,j)
                heappush(Q,(dist[i][j-1],i,j-1))
            if j < n-1 and dist[i][j+1] > d and dist[i][j+1] > abs(heights[i][j] - heights[i][j+1]):
                dist[i][j+1] = max(d, abs(heights[i][j]-heights[i][j+1]))
                parent[i][j+1] = (i, j)
                heappush(Q,(dist[i][j+1],i,j+1))

            if i > 0 and dist[i-1][j] > d and dist[i-1][j] > abs(heights[i][j] - heights[i-1][j]):
                dist[i-1][j] = max(d, abs(heights[i-1][j]-heights[i][j]))
                parent[i-1][j] = (i,j)
                heappush(Q,(dist[i-1][j],i-1,j))

            if i < m-1 and dist[i+1][j] > d and dist[i+1][j] > abs(heights[i+1][j] - heights[i][j]):
                dist[i+1][j] = max(d, abs(heights[i][j] - heights[i+1][j]))
                parent[i+1][j] = (i,j)
                heappush(Q,(dist[i+1][j],i+1,j))
        

        print(dist)
        print(parent)
        return dist[m-1][n-1]