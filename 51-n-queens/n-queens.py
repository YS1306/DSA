class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        all = [i for i in range(n)]
        filled = []
        r_dig = []   # i-j
        l_dig = []   # i+j
        def check(board, prev, idx, valid):
            if len(valid) != 0:
                for i in valid:
                    if i not in filled and (idx+i) not in l_dig and (idx-i) not in r_dig:
                        board[idx][i] = "Q"
                        filled.append(i)
                        r_dig.append(idx-i)
                        l_dig.append(idx+i)
                        valid2 = all.copy()
                        if i > 0 and i-1 in valid2:
                            valid2.remove(i-1)
                        if i < n-1 and i+1 in valid2:
                            valid2.remove(i+1)
                        if idx == n-1:
                            brd = []
                            for k in range(n):
                                brd.append(''.join(board[k]))
                            res.append(brd.copy())
                            board[idx][i] = "."
                            filled.remove(i)
                            r_dig.remove(idx-i)
                            l_dig.remove(idx+i)
                            continue 
                        check(board, prev, idx+1, valid2)
                        board[idx][i] = "."
                        filled.remove(i)
                        r_dig.remove(idx-i)
                        l_dig.remove(idx+i)
            return
        
        row = ["."]*n
        board = [row.copy() for j in range(n)]
        
        for j in range(n):
            board[0][j] = "Q"  
            filled.append(j)
            r_dig.append(-j)
            l_dig.append(j)
            valid2 = all.copy()
            if j > 0:
                valid2.remove(j-1)
            if j < n-1:
                valid2.remove(j+1)
            if n == 1:
                brd = []
                for k in range(n):
                    brd.append(''.join(board[k]))
                res.append(brd.copy())
                break 
            check(board, 0, 1, valid2)
            board[0][j] = "."
            filled.remove(j)
            r_dig.remove(-j)
            l_dig.remove(j)

        return res

