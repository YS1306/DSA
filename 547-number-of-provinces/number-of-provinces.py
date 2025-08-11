class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        visited = [False]*n
        # visited[0] = True
        count = 0
        def DFS(i):
            visited[i] = 1
            for j in range(n):
                if isConnected[i][j] == 1 and not visited[j]:
                    DFS(j)
        
        for i in range(n):
            if not visited[i]:
                visited[i] = True
                count += 1
                DFS(i)

        return count