class Solution:
    def trap(self, height: List[int]) -> int:
        stack = []
        last_box = 0; cnt = 0 ; res = 0
        for val in height:
            if not stack:
                if val:
                    stack.append(val)
                else:
                    continue
            elif stack and stack[-1] > val:
                stack.append(val)
            else:
                last_box = 0
                cnt = 0
                while(stack and stack[-1] < val):
                    last = stack.pop()
                    last_box += last
                    cnt += 1
                
                if stack:
                    last = stack[-1]
                else:
                    last_box -= last
                    cnt -= 1
                mini = min(val, last)
                box_l = (cnt+2)*mini
                fill = box_l - last_box - (mini<<1)
                res += fill
                
                if stack and (stack[:-1] or stack[-1] > val):
                    for i in range(cnt):
                        stack.append(val) 
                
                stack.append(val)              
                
            
        return res
            