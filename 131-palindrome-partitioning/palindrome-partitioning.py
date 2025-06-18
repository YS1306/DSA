class Solution:
    def partition(self, s: str) -> List[List[str]]:
    
        res = []

        def isPali(st):
            n = len(st)
            for i in range(n//2):
                if st[i] != st[n-i-1]:
                    return False

            return True

        def check(nums, curr_list):
            
            if len(nums) == 0:
                res.append(curr_list)
                return

            for i in range(1, len(nums)+1):
                
                if isPali(nums[:i]):
                    check(nums[i:], curr_list+[nums[:i]])

        check(s, [])
        return res