from heapq import heappush, heappop, heapify
class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        
        graph = {k:[] for k in range(n)}

        for i in range(len(edges)):
            graph[edges[i][0]].append((edges[i][1], succProb[i]))
            graph[edges[i][1]].append((edges[i][0], succProb[i]))

        dist = [0]*n
        q = []

        heappush(q, (-1, start_node))
        dist[start_node] = -1

        while(q):
            d, s = heappop(q)

            for node, prob in graph[s]:

                if dist[node] > d*prob:

                    dist[node] = d*prob
                    heappush(q, (dist[node], node))
        print(dist)
        return abs(dist[end_node])