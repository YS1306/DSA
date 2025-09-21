from heapq import heappush, heappop 
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = {i:[] for i in range(1,n+1)}    
        for u,v,w in times:
            graph[u].append((v,w))
        
        dist = [100000]*(n+1)
        q = []

        dist[k] = 0
        heappush(q, (0,k))

        while(q):
            d, s = heappop(q)

            for node, t in graph[s]:
                if dist[node] > d+t:
                    dist[node] = d+t
                    heappush(q, (dist[node], node))
            
        res = 0

        for k in dist[1:]:
            if k == 100000:
                return -1
            if k > res:
                res = k
        return res