class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        dist = [[float('inf')]*n for i in range(n)]
        reachable = {k:set() for k in range(n)}
        for i in range(n):
            dist[i][i] = 0
        for u,v,w in edges:
            dist[u][v] = w
            dist[v][u] = w

        for k in range(n):
            for i in range(n):
                for j in range(n):
                    if dist[i][j] > dist[i][k]+dist[k][j]:
                        dist[i][j] = dist[i][k]+dist[k][j]
                    # dist[i][j] = min(dist[i][j], dist[i][k]+dist[k][j])
        
        min_ctr = n+1
        city = n-1

        for i in range(n-1,-1,-1):
            ctr = 0
            for j in range(n):
                if dist[i][j] <= distanceThreshold:
                    ctr += 1

            if ctr < min_ctr:
                min_ctr = ctr
                city = i
        return city


