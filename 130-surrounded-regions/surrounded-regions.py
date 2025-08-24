class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m = len(board)
        n = len(board[0])
        visited = [[0 for j in range(n)] for i in range(m)]
        

        def dfs(i,j):
            board[i][j] = "F"
            if j < n-1 and not visited[i][j+1] and board[i][j+1] == "O":
                visited[i][j+1] = 1
                dfs(i,j+1)
            if j > 0 and not visited[i][j-1] and board[i][j-1] == "O":
                visited[i][j-1] = 1
                dfs(i, j-1)
            if i < m-1 and not visited[i+1][j] and board[i+1][j] == "O":
                visited[i+1][j] = 1
                dfs(i+1,j)
            if i > 0 and not visited[i-1][j] and board[i-1][j] == "O":
                visited[i-1][j] = 1
                dfs(i-1, j)            

                
            
        for i in range(m):
            if board[i][0] == "O":
                dfs(i,0)
            if board[i][n-1] == "O":
                dfs(i,n-1)
        
        for j in range(n):
            if board[0][j] == "O":
                dfs(0,j)
            if board[m-1][j] == "O":
                dfs(m-1,j)
                
        
        for i in range(m):
            for j in range(n):
                if board[i][j] == "O":
                    board[i][j] = "X"
                if board[i][j] == "F":
                    board[i][j] = "O"



        