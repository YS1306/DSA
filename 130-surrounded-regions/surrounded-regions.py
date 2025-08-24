class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m = len(board)
        n = len(board[0])
        visited = [[0 for j in range(n)] for i in range(m)]
        
        region = []

        def dfs(i,j):
            if i in [0,m-1] or j in [0, n-1]:
                return False
            v1 = True
            v2 = True
            v3 = True
            v4 = True

            if j < n-1 and not visited[i][j+1] and board[i][j+1] == "O":
                region.append((i,j+1))
                visited[i][j+1] = 1
                v1 = dfs(i,j+1)
            if j > 0 and not visited[i][j-1] and board[i][j-1] == "O":
                region.append((i,j-1))
                visited[i][j-1] = 1
                v2 = dfs(i, j-1)
            if i < m-1 and not visited[i+1][j] and board[i+1][j] == "O":
                region.append((i+1,j))
                visited[i+1][j] = 1
                v3 = dfs(i+1,j)
            if i > 0 and not visited[i-1][j] and board[i-1][j] == "O":
                region.append((i-1,j))
                visited[i-1][j] = 1
                v4 = dfs(i-1, j)
            
            if v1 and v2 and v3 and v4:
                return True
            else:
                return False
                

        
        for i in range(m):
            for j in range(n):
                if board[i][j] == "O" and not visited[i][j]:
                    region.append((i,j))
                    val = dfs(i,j)
                    if val:
                        for ind in region:
                            r,c = ind
                            board[r][c] = "X"
                
                region = []



        