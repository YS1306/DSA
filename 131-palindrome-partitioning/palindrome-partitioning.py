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
            flag = True
            if len(curr_list) > 0: 

                temp = curr_list[-1]
                n = len(temp)
                for i in range(n//2):
                    if temp[i] != temp[n-i-1]:
                        flag = False
                        break

            if not flag:
                return
            if len(nums) == 0:
                if flag:
                    res.append(curr_list)
                return

            for i in range(1, len(nums)+1):
                check(nums[i:], curr_list+[nums[:i]])

        check(s, [])
        return res