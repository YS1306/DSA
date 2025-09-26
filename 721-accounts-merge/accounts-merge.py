from collections import defaultdict
class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        parent  = [i for i in range(len(accounts))]
        belongsTo = defaultdict(lambda: -1)
        
        def findP(u):
            if parent[u] == u:
                return u
            parent[u] = findP(parent[u])
            return parent[u]
        
        def Union(u, v):
            par_u = findP(u)
            par_v = findP(v)

            parent[par_v] = par_u


        for i in range(len(accounts)):
            for email in accounts[i][1:]:
                if belongsTo[email] != -1:
                    Union(belongsTo[email], i)
                else:
                    belongsTo[email] = i

    
        
        mails = defaultdict(list)
        for mail, ind in belongsTo.items():
            mails[findP(ind)].append(mail)
        
        res = []
        for ind, mail in mails.items():
            res.append([accounts[ind][0]]+sorted(mail))

        return res