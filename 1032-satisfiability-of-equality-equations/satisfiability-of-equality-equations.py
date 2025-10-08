class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        parent = dict()
        p_keys = set()
        def find(node):
            if node not in p_keys:
                parent[node] = node
                p_keys.add(node)
                return node
            if parent[node] == node:
                return node
            parent[node] = find(parent[node])
            return parent[node]
        
        def Union(i, j, comp):
            p1 = find(i)
            p2 = find(j)
            if comp == 1 and p1 == p2:
                return False
            if comp == 0:
                if p1 < p2:
                    parent[p1] = p2 
                else:
                    parent[p2] = p1
            
            return True
        
        not_equals = [] 
        for eqn in equations:
            i, comp, j = eqn[0] , (eqn[1:3] == "!="), eqn[3] 
            if comp == 1:
                not_equals.append((i, j, comp))
            else:
                curr = Union(i, j, comp)
        
        for i, j, comp in not_equals:
            curr = Union(i, j, comp)
            if not curr:
                return False

        return True