class Solution:
    # def myAtoi(self, s: str) -> int:
    #     # print(s)
    #     if(len(s) == 0):
    #         return 0
    #     if len(s) == 1:
    #         if(s[0] >= '0' and s[0]<='9'):
    #             return int(s[0])
    #         else:
    #             return 0
    #     if s[0] == '0' and (s[1] >= '0' and s[1]<='9'):
    #         return  max(min(self.myAtoi(s[1:]), 2**31-1), 2**-31)
    #     if(s[0] == ' ' and ((s[1] >= '0' and s[1]<='9') or (s[1] in [' ', '-', '+']))):
    #         return self.myAtoi(s[1:])
    #     if(s[0] == '-' and s[1] >= '0' and s[1]<='9'):
    #         return -1*max(min(self.myAtoi(s[1:]), 2**31-1), 2**-31)
    #     if(s[0] == '+' and s[1] >= '0' and s[1]<='9'):
    #         return max(min(self.myAtoi(s[1:]), 2**31-1), 2**-31)
    #     if(s[0] > '0' and s[0]<='9' ):
    #         if(s[1] >= '0' and s[1]<='9'):
    #             next = self.myAtoi(s[1:])
    #             print(next)
    #             curr = int(s[0])
    #             if(next == 0):
    #                 return curr*10
    #             if(curr > int(s[1])):
    #                 while(curr < next*10):
    #                     curr = curr*10
    #             else:
    #                 while(curr < next):
    #                     # print(curr, next)
    #                     curr = curr*10
    #             return max(min(curr+next, 2**31-1), 2**-31)
    #         else:
    #             return int(s[0])
    #     # if(s[0] < '0' or s[0] > '9'):
    #     return 0
    #     # else:

    digits = 0

    def Atoi(self, s:str, sign:int):
        if(len(s) == 0):
            return 0
        # if(len(s) == 1 and )
        
        if(s[0] in [' ', '+', '-']):
            return 0
        
        if(s[0] >= '0' and s[0] <= '9'):
            res = self.Atoi(s[1:], sign)
            self.digits += 1
            if(sign == -1):
                return min(10**(self.digits-1)*int(s[0])+res, 2**(31))
            else:
                return min(10**(self.digits-1)*int(s[0])+res, 2**(31)-1)
        return 0
    def myAtoi(self, s: str) -> int:
        if(len(s) == 0):
            return 0
        while(s[0] == ' '):
            return self.myAtoi(s[1:])
        if(s[0] == '-'):
            sign = -1
            return -1*self.Atoi(s[1:], sign)
        if(s[0]== '+'):
            sign = 1
            return self.Atoi(s[1:], sign)
        return self.Atoi(s, 1)
