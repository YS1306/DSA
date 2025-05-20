class Solution:
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
