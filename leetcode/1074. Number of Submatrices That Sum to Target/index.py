from collections import defaultdict
from typing import List


class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        rows = len(matrix)
        cols = len(matrix[0])
        res = 0
        for row in range(rows):
            for col in range(1, cols):
                matrix[row][col] += matrix[row][col-1]
        for colRight in range(cols):
            for colLeft in range(colRight+1):
                total = 0
                pre = defaultdict(int)
                pre[0] = 1
                for row in range(rows):
                    total += matrix[row][colRight] - (matrix[row][colLeft-1] if colLeft >= 1 else 0)
                    res += pre[total-target]
                    pre[total] += 1
        return res

solution = Solution()
matrix = [[0,1,0],[1,1,1],[0,1,0]]
target = 0
assert solution.numSubmatrixSumTarget(matrix, target) == 4, "Should be 4"