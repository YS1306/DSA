class Solution:
    def asteroidCollision(self, arr: List[int]) -> List[int]:
        stack = []

        for i in range(len(arr)):
            curr = arr[i]
            if not stack or (stack[-1] > 0 and curr > 0) or (stack[-1] < 0 and curr < 0) or (curr > 0 and stack[-1] < 0):
                stack.append(curr)
            
            elif curr < 0 and stack[-1] > 0:
                flag = False
                while(stack and stack[-1] > 0 and stack[-1] < abs(curr)):
                    flag = True
                    stack.pop()
                    
                if stack and stack[-1] > 0 and stack[-1] == abs(curr):
                    stack.pop()
                    continue
                elif stack and stack[-1] > 0 and stack[-1] > abs(curr):
                    flag = False
                elif flag:
                    stack.append(curr)
        return stack
                 