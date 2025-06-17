class Solution:
    def partition(self, s: str) -> List[List[str]]:
        #go upto full 

        #check from last
        # call check, if check returns True upto last -> append all to res

        # Take 1 element in set and call for next, then 2 in set, then 

        # if curr[-1] not palindrome    return
        # if idx = -1: if palindrome append curr
        res = []

        def isPali(st):
            n = len(st)
            for i in range(n//2):
                if st[i] != st[n-i-1]:
                    return False

            return True

        def check(nums, curr_list, idx):
            # print(curr_list, nums, idx)
            if len(curr_list) > 0 and not isPali(curr_list[-1]):
                # print("YES")
                return
            if len(nums) == 0:
                if isPali(curr_list[-1]):
                    res.append(curr_list)
                return
            # print("2nd  ",curr_list+[nums[1:1+1]])
            for i in range(1, len(nums)+1):
                check(nums[idx+i:], curr_list+[nums[idx:idx+i]], 0)

        check(s, [], 0)
        return res