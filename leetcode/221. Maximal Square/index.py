from typing import List


class Solution:
    # brute force
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        rows, cols = len(matrix), len(matrix[0])
        res = 0
        for row in range(rows):
            for col in range(cols):
                if matrix[row][col] == '1':
                    length = 1
                    stop = False
                    while (row+length) < rows and (col+length) < cols and not stop:
                        for r in range(row, row+length+1):
                            if matrix[r][col+length] == '0':
                                stop = True
                                break
                        for c in range(col, col+length+1):
                            if matrix[row+length][c] == '0':
                                stop = True
                                break
                        if not stop:
                            length += 1
                    res = max(res, length)
        return res ** 2
    # dp
    def maximalSquare1(self, matrix: List[List[str]]) -> int:
        rows, cols = len(matrix), len(matrix[0])
        prev, cur = [0] * cols, [0] * cols
        res = 0
        for row in range(rows):
            for col in range(cols):
                if matrix[row][col] == '1':
                    cur[col] = min(prev[col-1] if col > 0  else 0,
                                prev[col],
                                cur[col-1] if col > 0 else 0) + 1
                    res = max(cur[col], res)
            prev, cur = cur, [0] * cols
        return res ** 2

solution = Solution()
matrix = [["0","0","0","1","0","1","1","1"],["0","1","1","0","0","1","0","1"],["1","0","1","1","1","1","0","1"],["0","0","0","1","0","0","0","0"],["0","0","1","0","0","0","1","0"],["1","1","1","0","0","1","1","1"],["1","0","0","1","1","0","0","1"],["0","1","0","0","1","1","0","0"],["1","0","0","1","0","0","0","0"]]
assert solution.maximalSquare(matrix) == 1, "Should be 1"
assert solution.maximalSquare1(matrix) == 1, "Should be 1"