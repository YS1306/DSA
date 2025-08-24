class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        visited = [[0 for j in range(n)] for i in range(m)]
        

        def dfs(i,j):
            grid[i][j] = 2
            if j < n-1 and not visited[i][j+1] and grid[i][j+1] == 1:
                visited[i][j+1] = 1
                dfs(i,j+1)
            if j > 0 and not visited[i][j-1] and grid[i][j-1] == 1:
                visited[i][j-1] = 1
                dfs(i, j-1)
            if i < m-1 and not visited[i+1][j] and grid[i+1][j] == 1:
                visited[i+1][j] = 1
                dfs(i+1,j)
            if i > 0 and not visited[i-1][j] and grid[i-1][j] == 1:
                visited[i-1][j] = 1
                dfs(i-1, j)   

        
        for i in range(m):
            if grid[i][0] == 1:
                dfs(i,0)
            if grid[i][n-1] == 1:
                dfs(i,n-1)
        
        for j in range(n):
            if grid[0][j] == 1:
                dfs(0,j)
            if grid[m-1][j] == 1:
                dfs(m-1,j)

        count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    count += 1

        return count