class Solution:
    def numTrees(self, n: int) -> int:
        dp = [1] * (n+1)
        dp[1] = 1
        for i in range(2, n+1):
            total = 0
            for index in range(i):
                total += dp[index] * dp[i - index - 1]
            dp[i] = total
        return dp[n]


solution = Solution()
assert solution.numTrees(3) == 5, "Should be 5"
