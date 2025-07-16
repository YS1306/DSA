class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        close = {')':'(', ']':'[' , '}':'{' }
        for i in s:
            # print(stack, i)
            if i in ['(', '[', '{']:
                # print(i, True)
                stack.append(i)
            else:
                if len(stack) > 0 and stack[-1] == close[i]:
                    stack.pop()
                else:
                    return False
        
        return len(stack) == 0