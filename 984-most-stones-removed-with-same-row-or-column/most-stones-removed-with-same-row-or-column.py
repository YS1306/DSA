class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        n = len(stones)
        parent = [i for i in range(n)]
        size = [1]*n


        def findP(u):
            if parent[u] == u:
                return u
            parent[u] = findP(parent[u])
            return parent[u]

        def UnionBySize(u,v):
            par_u = findP(u)
            par_v = findP(v)

            if par_u == par_v:
                return size[par_u]
            
            if size[par_u] < size[par_v]:
                parent[par_u] = par_v
                size[par_v] += size[par_u]
            else:
                parent[par_v] = par_u 
                size[par_u] += size[par_v]
            

        for i in range(len(stones)):
            x1, y1 = stones[i]
            for j in range(i+1,len(stones)):
                x2, y2 = stones[j]
                if (x1 == x2) or (y1 == y2):
                    UnionBySize(i, j)

        res = 0
        for i in range(n):
            if parent[i] == i:
                res += 1

        return n-res
