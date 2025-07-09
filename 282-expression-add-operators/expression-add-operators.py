class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        res = []


        def check(num, curr, target):
            # print(curr)
            if eval(curr) == target and curr not in res and len(num) == 0:
                # try:
                #     int(curr)
                # except:
                res.append(curr)
                return
            # print(curr, eval(curr))
            
            if len(num) == 0:
                return
            # print(curr)
            
            if (len(curr) == 1 and not(curr[-1] == '0')) or (len(curr) >= 2 and not ( curr[-1] == '0' and curr[-2] in ["+", "-", "*"])):
                curr0 = curr+num[0]
                check(num[1:], curr0, target)
        
            
            curr1 = curr+f"+{num[0]}"
            # print(curr1, num[0])
            check(num[1:], curr1, target)
            

            curr2 = curr+f"*{num[0]}"
            check(num[1:], curr2, target)

            curr3 = curr+f"-{num[0]}"
            check(num[1:], curr3, target)
                
            return 

        check(num[1:], num[0], target)

        # print(len(res))
        
        
        return sorted(res)

        