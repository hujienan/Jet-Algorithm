class Solution:
    def numTrees(self, n: int) -> int:
        dp = [1] * (n+1)
        for nodes in range(2, n+1):
            total = 0
            for i in range(1, nodes+1):
                total += dp[i-1] * dp[nodes-i]
            dp[nodes] = total
        return dp[n]


solution = Solution()
assert solution.numTrees(3) == 5, "Should be 5"
