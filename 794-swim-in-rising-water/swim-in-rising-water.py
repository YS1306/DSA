from heapq import heappush, heappop
class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        dist = [[float('inf') for i in range(n)] for i in range(n)]
        q = []

        heappush(q, (grid[0][0], 0, 0))
        dist[0][0] = grid[0][0]

        while(q):
            d, i, j = heappop(q)
            if (i, j) == (n-1, n-1):
                return dist[n-1][n-1]

            if j < n-1 and dist[i][j+1] > max(grid[i][j+1], d):
                dist[i][j+1] = max(grid[i][j+1], d)
                heappush(q, (dist[i][j+1], i, j+1))
            if i < n-1 and dist[i+1][j] > max(grid[i+1][j], d):
                dist[i+1][j] = max(grid[i+1][j], d)
                heappush(q, (dist[i+1][j], i+1, j))
            if j > 0 and dist[i][j-1] > max(grid[i][j-1], d):
                dist[i][j-1] = max(grid[i][j-1], d)
                heappush(q, (dist[i][j-1], i, j-1))
            if i > 0 and dist[i-1][j] > max(grid[i-1][j], d):
                dist[i-1][j] = max(grid[i-1][j], d)
                heappush(q, (dist[i-1][j], i-1, j))

        return grid[n-1][n-1]