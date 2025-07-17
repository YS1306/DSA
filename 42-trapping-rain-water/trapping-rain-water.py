class Solution:
    def trap(self, height: List[int]) -> int:
        stack = []; stack2 = []
        last_box = 0; cnt = 0 ; res = 0
        for val in height:
            if not stack:
                if val:
                    stack.append(val)
                else:
                    continue
            elif stack and stack[-1] > val:
                stack.append(val)
                # last_box += val
            else:
                i = 1
                last_box = 0
                cnt = 0
                stack2 = []
                while(stack and stack[-1] < val):
                    last = stack.pop()
                    stack2.append(last)
                    last_box += last
                    cnt += 1
                
                if stack:
                    last = stack[-1]
                else:
                    last_box -= last
                    cnt -= 1
                    
                
                box_l = (cnt+2)*min(val, last)
                fill = box_l - last_box - (2*min(val,last))
                res += fill
                
                if stack and (stack[:-1] or stack[-1] > val):
                    while(stack2):
                        stack2.pop()
                        stack.append(val)
                
                stack.append(val)              
                
            
        return res
            