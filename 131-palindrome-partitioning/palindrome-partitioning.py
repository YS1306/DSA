class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []

        

        def check(nums, curr_list):
            def isPali(st):
                n = len(st)
                for i in range(n//2):
                    if st[i] != st[n-i-1]:
                        return False

                return True

            if len(curr_list) > 0 and not isPali(curr_list[-1]):
                return
            if len(nums) == 0:
                if isPali(curr_list[-1]):
                    res.append(curr_list)
                return

            for i in range(1, len(nums)+1):
                check(nums[i:], curr_list+[nums[:i]])

        check(s, [])
        return res