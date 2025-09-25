class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        
        parent = [i for i in range(n)]
        size = [1]*n
        res = 0

        def find(u):
            if parent[u] == u:
                return u
            parent[u] = find(parent[u])
            return parent[u]

        def UnionBySize(res, u,v):
            par_u = find(u)
            par_v = find(v)

            if par_u == par_v:
                res += 1
            elif size[par_u] < size[par_v]:
                parent[par_u] = par_v
                size[par_v] += size[par_u]
            else:
                parent[par_v] = par_u
                size[par_u] += size[par_v]

            # print(par_u, par_v)
            
            return res
            
        for u, v in connections:
            res = UnionBySize(res, u,v)
        comp = 0
        for node in range(n):
            if parent[node] == node:
                comp +=1 

        # comp = len(set(parent))
        
        if res >= comp-1:
            return comp-1
        return -1

            