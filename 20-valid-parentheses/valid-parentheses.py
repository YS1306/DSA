# from collections import deque
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        close = {')':'(', ']':'[' , '}':'{' }
        for i in s:
            if i in ['(', '[', '{']:
                stack.append(i)
            else:
                if len(stack) > 0 and stack[-1] == close.get(i):
                    stack.pop()
                else:
                    return False
        
        return len(stack) == 0