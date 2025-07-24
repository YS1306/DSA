class Solution:
    def asteroidCollision(self, arr: List[int]) -> List[int]:
        stack = []

        for i in range(len(arr)):
            curr = arr[i]
            flag = True
            
            if stack and curr < 0 < stack[-1]:
                flag = False
                while(stack and stack[-1] > 0 and stack[-1] < abs(curr)):
                    flag = True
                    stack.pop()
                    
                if stack and stack[-1] > 0 and stack[-1] == abs(curr):
                    stack.pop()
                    continue
                elif stack and stack[-1] > 0 and stack[-1] > abs(curr):
                    flag = False

            if flag:
                stack.append(curr)
        return stack
                 