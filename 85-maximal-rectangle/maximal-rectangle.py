class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
    
        m = len(matrix)
        n = len(matrix[0])
        heights = [0]*n
        res = 0
        for i in range(m):
            stack = []
            pse_arr = [-1]*n
            for j in range(n):
                if matrix[i][j] == "0":
                    heights[j] = 0
                else:
                    heights[j] += 1

                while(stack and heights[stack[-1]] >= heights[j]):
                    temp = stack.pop()
                    val = (j-pse_arr[temp]-1)*heights[temp]
                    # print(j, temp, val)
                    if res < val:
                        res = val

                if stack:
                    pse_arr[j] = stack[-1]
                stack.append(j)
            
            while(stack):
                temp = stack.pop()
                val = (n-pse_arr[temp]-1)*heights[temp]
                # print(val)
                if res < val:
                    res = val
            # print(heights)
        return res
         
