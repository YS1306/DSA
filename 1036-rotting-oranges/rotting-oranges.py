from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        def solver(grid):
            m = len(grid)
            n = len(grid[0])
            q = deque()
            visited = []
            total = 0
            rotten = 0

            for i in range(m):
                for j in range(n):
                    if grid[i][j] > 0:
                        if grid[i][j] == 2:
                            q.append((i,j))
                            rotten += 1
                        # if grid[i][j] == 1:
                        total += 1
            
            if total == rotten:
                return 0

            count = 0
            next_q = deque()
            flag = False
            while(q or next_q):
                curr = q.popleft()
                # print(grid[curr[0]][curr[1]] == 1)
                if curr in visited:
                    # print(curr)
                    continue
                visited.append(q)
                r,c = curr
                
                if c < n-1 and grid[r][c+1] == 1:
                    grid[r][c+1] = 2
                    next_q.append((r, c+1))
                    rotten += 1
                    flag = True
                if r < m-1 and grid[r+1][c] == 1:
                    grid[r+1][c] = 2
                    next_q.append((r+1,c))
                    rotten += 1
                    flag = True
                if c > 0 and grid[r][c-1] == 1:
                    grid[r][c-1] = 2
                    next_q.append((r, c-1))
                    rotten += 1
                    flag = True
                
                if r > 0 and grid[r-1][c] == 1:
                    grid[r-1][c] = 2
                    next_q.append((r-1, c))
                    rotten += 1
                    flag = True
                
                # print(q, next_q)
                if not q and next_q:
                    q = next_q.copy()
                    next_q = deque()
                    if flag:
                        count += 1
                    flag = False
                    
                
                # if flag:
                    # count += 1 
            # print("count",count,"total" ,total,"rotten", rotten)
            if total == rotten:
                return count
            else:
                return -1

        grid2 = [[0 for i in range(m)] for j in range(n)]

        for i in range(n):
            for j in range(m):
                grid2[i][j] = grid[j][i]
        

        # grid2 = [grid[j][i] for j in range(n) for i in range(m)]
        
        c1 = solver(grid)
        c2 = solver(grid2)
        print(c1, c2)
        return min(c1, c2)