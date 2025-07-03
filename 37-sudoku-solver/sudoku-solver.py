from typing import List

class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        n = 9
        rows = [set() for _ in range(n)]
        cols = [set() for _ in range(n)]
        boxes = [set() for _ in range(n)]

        # initialize sets
        for i in range(n):
            for j in range(n):
                if board[i][j] != ".":
                    v = board[i][j]
                    rows[i].add(v)
                    cols[j].add(v)
                    boxes[(i//3)*3 + j//3].add(v)

        def backtrack() -> bool:
            # choose the empty cell with the fewest possibilities
            min_count = 10
            target = None
            for i in range(n):
                for j in range(n):
                    if board[i][j] == ".":
                        b = (i//3)*3 + j//3
                        candidates = [c for c in map(str, range(1, n+1))
                                      if c not in rows[i] and c not in cols[j] and c not in boxes[b]]
                        if not candidates:
                            return False
                        if len(candidates) < min_count:
                            min_count = len(candidates)
                            target = (i, j, candidates)
            # if no empty cells remain, solution found
            if not target:
                return True

            i, j, candidates = target
            b = (i//3)*3 + j//3
            for c in candidates:
                board[i][j] = c
                rows[i].add(c)
                cols[j].add(c)
                boxes[b].add(c)
                if backtrack():
                    return True
                board[i][j] = "."
                rows[i].remove(c)
                cols[j].remove(c)
                boxes[b].remove(c)
            return False

        backtrack()