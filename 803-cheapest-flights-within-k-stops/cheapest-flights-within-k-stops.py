from heapq import heappush, heappop
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:

        graph = {k:[] for k in range(n)}

        for s,t,p in flights:
            graph[s].append((t, p))

        dist = [10000000]*n
        dist[src] = 0
        q = []
        heappush(q, (0,src,0))

        while(q):
            stop, node, d = heappop(q)
            if stop > k or node == dst:
                continue

            for n,p in graph[node]:
                if dist[n] > d+p:
                    dist[n] = d+p
                    heappush(q, (stop+1, n, dist[n]))
                
        if dist[dst]  != 10000000:
            return dist[dst]
        else:
            return -1
