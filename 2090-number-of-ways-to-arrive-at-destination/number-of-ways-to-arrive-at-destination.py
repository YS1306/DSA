class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        graph = {i:[] for i in range(n)}

        for u,v,t in roads:
            graph[u].append((v,t))
            graph[v].append((u,t))

        dist = [float('inf')]*n
        ways = [0]*n
        q = []

        dist[0] = 0
        ways[0] = 1
        # q.append((dist[0],0))
        heappush(q, (dist[0], 0))
        
        while(q):
            d, s = heappop(q)
            if dist[s] < d:
                continue
            
            for node, t in graph[s]:
                if dist[node] > (d+t):
                    dist[node] = d+t
                    ways[node] = ways[s]
                    # q.append((d+t, node))
                    heappush(q, (d+t,node))
                elif dist[node] == (d+t):
                    ways[node] = (ways[node]+ways[s])%int(1e9+7)

        return ways[n-1]%int(1e9+7)
