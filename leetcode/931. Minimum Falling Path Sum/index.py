from typing import List


class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        rows = len(matrix)
        cols = len(matrix[0])
        dp = [[0 for _ in range(cols)] for _ in range(rows)]
        dp[0] = matrix[0]
        for row in range(1, rows):
            for col in range(cols):
                temp = [dp[row - 1][col]]
                if col - 1 >= 0:
                    temp.append(dp[row - 1][col - 1])
                if col + 1 < cols:
                    temp.append(dp[row - 1][col + 1])
                dp[row][col] = matrix[row][col] + min(temp)
        return min(dp[rows - 1])


solution = Solution()
matrix = [[2, 1, 3], [6, 5, 4], [7, 8, 9]]
assert solution.minFallingPathSum(matrix) == 13, "Should be 13"
