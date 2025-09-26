import copy
class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        ctr = -1
        belongsTo = defaultdict(int)
        n = len(grid)
        visited = [[False for j in range(n)] for i in range(n)]
        size = []
        def dfs(par, i, j):
            belongsTo[(i,j)] = par
            size[-1] += 1
            if j < n-1 and not visited[i][j+1] and grid[i][j+1]:
                visited[i][j+1] = True
                dfs(par, i, j+1)
            if i < n-1 and not visited[i+1][j] and grid[i+1][j]:
                visited[i+1][j] = True
                dfs(par, i+1, j)
            if j > 0 and not visited[i][j-1] and grid[i][j-1]:
                visited[i][j-1] = True
                dfs(par, i, j-1)
            if i > 0 and not visited[i-1][j] and grid[i-1][j]:
                visited[i-1][j] = True
                dfs(par, i-1, j)
        
        par = 0
        cands = []
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 0:
                    cands.append((i,j))
                elif not visited[i][j]:
                    visited[i][j] = True
                    size.append(0)
                    dfs(par, i, j)
                    par += 1

        parent = [i for i in range(par+1)]
        size.append(0)
        largest = max(size)

        ctr = par

        for i, j in cands:
            curr = 1
            neighbours = set()
            if j < n-1 and grid[i][j+1]:
                neighbours.add(belongsTo[(i,j+1)])

            if i < n-1 and grid[i+1][j]:
                neighbours.add(belongsTo[(i+1, j)])

            if j > 0 and grid[i][j-1]:
                neighbours.add(belongsTo[(i,j-1)])

            if i > 0 and grid[i-1][j]:
                neighbours.add(belongsTo[(i-1,j)])
            
            for island in neighbours:
                curr += size[island]

            if curr > largest:
                largest = curr


        return largest