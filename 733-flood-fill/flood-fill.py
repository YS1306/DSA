from collections import deque
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        m = len(image)
        n = len(image[0])
        init = image[sr][sc]
        q = deque()
        q.append((sr,sc))
        if image[sr][sc] == color:
            return image
        else:
            image[sr][sc] = color
            
        while(q):
            curr = q.popleft()
            r, c = curr

            if r < m-1 and image[r+1][c] == init:
                image[r+1][c] = color
                q.append((r+1,c))
            if r >0 and image[r-1][c] == init:
                image[r-1][c] = color
                q.append((r-1,c))
            if c < n-1 and image[r][c+1] == init:
                image[r][c+1] = color
                q.append((r, c+1))
            if c > 0 and image[r][c-1] == init:
                image[r][c-1] = color
                q.append((r, c-1))
            
        return image