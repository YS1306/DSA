class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res = []
        lim = min(9,n)
        def check(m, curr_list, target):
            
            if len(curr_list) == k:
                if target == 0:
                    res.append(curr_list)
                return
            
            if m > lim:
                return
            
            check(m+1, curr_list+[m], target-m)
            check(m+1, curr_list, target)


        check(1, [], n)
        return res