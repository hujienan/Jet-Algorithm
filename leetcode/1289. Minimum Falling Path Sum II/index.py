from typing import List


class Solution:
    def minFallingPathSum(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        dp = [[0 for _ in range(cols)] for _ in range(rows)]
        dp[0] = grid[0]
        for row in range(1, rows):
            for col in range(cols):
                temp = dp[row - 1][:col] + dp[row - 1][col + 1 :]
                dp[row][col] = grid[row][col] + min(temp)
        return min(dp[rows - 1])


solution = Solution()
grid = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
assert solution.minFallingPathSum(grid) == 13, "Should be 13"
