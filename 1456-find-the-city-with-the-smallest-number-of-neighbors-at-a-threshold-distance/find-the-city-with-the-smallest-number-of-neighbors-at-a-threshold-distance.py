class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        dist = [[float('inf')]*n for i in range(n)]
        reachable = {k:set() for k in range(n)}
        for i in range(n):
            dist[i][i] = 0
        for u,v,w in edges:
            dist[u][v] = w
            dist[v][u] = w

            if w < distanceThreshold:
                reachable[u].add(v)
                reachable[v].add(u)

        for k in range(n):
            for i in range(n):
                for j in range(n):
                    dist[i][j] = min(dist[i][j], dist[i][k]+dist[k][j])
                    if dist[i][j] <= distanceThreshold:
                        reachable[i].add(j)
                        reachable[j].add(i)

        min_ctr = n+1
        city = n-1

        for i in range(n-1,-1,-1):
            if len(reachable[i]) < min_ctr:
                min_ctr = len(reachable[i])
                city = i

        return city


