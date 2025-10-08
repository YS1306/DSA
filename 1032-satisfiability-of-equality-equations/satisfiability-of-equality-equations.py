class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        equal = set()
        not_equal = set()
        parent = dict()
        
        def find(node):
            if parent.get(node, -1) == -1:
                parent[node] = node
                return node
            if parent[node] == node:
                return node
            parent[node] = find(parent[node])
            return parent[node]
        
        def Union(i, j, comp):
            p1 = find(i)
            p2 = find(j)
            print(i, j, p1, p2)
            if comp == 1 and p1 == p2:
                return False
            if comp == 0:
                if p1 < p2:
                    parent[p1] = p2 
                else:
                    parent[p2] = p1
            
            return True
        
        not_equals = [] 
        equals = []
        for eqn in equations:
            i, comp, j = eqn[0] , (eqn[1:3] == "!="), eqn[3] 
            if comp == 1:
                not_equals.append((i, j, comp))
            else:
                curr = Union(i, j, comp)
        
        print(parent)
        for i, j, comp in not_equals:
            curr = Union(i, j, comp)
            if not curr:
                return False

        return True