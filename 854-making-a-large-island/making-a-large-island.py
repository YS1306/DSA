import copy
class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        # grid = [[0 for j in range(m)] for i in range(n)]
        
        
        
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
        
        # print(parent)
        # print(size)

        def UnionBySize(parent, size, u, v):
            # def findP(u):
            #     if parent[u] == u:
            #         return u
            #     parent[u] = findP(parent[u])
            #     return parent[u]
            # print(u, v)
            par_u = parent[u];   par_v = parent[v]
            if par_u == par_v:
                # return par_v
                return parent, size, par_u, size[par_u]
            
        
            parent[par_v] = par_u
            size[par_u] += size[par_v];     size[par_v] = 0
            return parent, size, par_u, size[par_u]
            

        def process(parent, size, belongsTo, i, j):
            curr_large = 1
            belongsTo[(i, j)] = par
            if j < n-1 and grid[i][j+1]:
                parent, size, new, upd = UnionBySize(parent, size, belongsTo[(i,j+1)], belongsTo[(i,j)])        
                if upd > curr_large:
                    curr_large = upd
                belongsTo[(i,j)] = new
                # visited[i][j] = True
                # dfs(par, i, j+1)
            if i < n-1 and grid[i+1][j]:
                parent, size, new, upd = UnionBySize(parent, size, belongsTo[(i+1,j)], belongsTo[(i,j)])
                if upd > curr_large:
                    curr_large = upd
                belongsTo[(i, j)] = new
                # belongsTo[(i,j)] = new
                # visited[i][j] = True
                # dfs(par, i+1, j)
            if j > 0 and grid[i][j-1]:
                parent, size, new, upd = UnionBySize(parent, size, belongsTo[(i,j-1)], belongsTo[(i,j)])
                if upd > curr_large:
                    curr_large = upd
                belongsTo[(i,j)] = new
                # visited[i][j] = True
                # dfs(par, i, j-1)
            if i > 0 and grid[i-1][j]:
                parent, size, new, upd = UnionBySize(parent, size, belongsTo[(i-1, j)], belongsTo[(i,j)])
                if upd > curr_large:
                    curr_large = upd
                belongsTo[(i,j)] = new
                # visited[i][j] = True
                # dfs(par, i-1, j)
            return curr_large

        ctr = par

        # parent_copy = copy.deepcopy(parent)
        # size_copy = copy.deepcopy(size)
        for i, j in cands:
            curr = 1
            neighbours = set()
            if j < n-1 and grid[i][j+1]:
                neighbours.add(belongsTo[(i,j+1)])

            if i < n-1 and grid[i+1][j]:
                # curr += size[]
                neighbours.add(belongsTo[(i+1, j)])

            if j > 0 and grid[i][j-1]:
                # curr += size[]
                neighbours.add(belongsTo[(i,j-1)])

            if i > 0 and grid[i-1][j]:
                # curr += size[]
                neighbours.add(belongsTo[(i-1,j)])
            
            for island in neighbours:
                curr += size[island]
                
            if curr > largest:
                largest = curr

            # grid[i][j] = 1
            # belongsTo[(i,j)] = ctr
            # parent[ctr] = ctr
            # size[ctr] = 1
            
            # curr = process(parent.copy(), size.copy(), belongsTo, i, j)


            # if curr > largest:
            #     largest = curr

            # grid[i][j] = 0

        return largest