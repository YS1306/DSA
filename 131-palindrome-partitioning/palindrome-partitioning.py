class Solution:
    def isPali(self, st):
            n = len(st)
            for i in range(n//2):
                if st[i] != st[n-i-1]:
                    return False

            return True

    def partition(self, s: str) -> List[List[str]]:
    
        res = []

        

        def check(nums, curr_list):
            
            if len(nums) == 0:
                res.append(curr_list)
                return

            for i in range(1, len(nums)+1):
                
                if self.isPali(nums[:i]):
                    check(nums[i:], curr_list+[nums[:i]])

        check(s, [])
        return res