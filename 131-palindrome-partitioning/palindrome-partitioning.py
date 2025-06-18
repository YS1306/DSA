class Solution:
    def partition(self, s: str) -> List[List[str]]:
    
        res = []

        def check(nums, curr_list):
            
            if len(nums) == 0:
                res.append(curr_list)
                return

            for i in range(1, len(nums)+1):
                flag = True
                temp = nums[:i]
                n = len(temp)
                for j in range(n//2):
                    if temp[j] != temp[n-j-1]:
                        flag = False
                        break

                if flag:
                    check(nums[i:], curr_list+[nums[:i]])

        check(s, [])
        return res