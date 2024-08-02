class Solution:
    def dieSimulator(self, n: int, rollMax: list[int]) -> int:
        dp = [[[0] * 16 for _ in range(6)] for _ in range(n)]
        for roll in range(6):
            dp[0][roll][1] = 1
        for i in range(1, n):
            for j in range(6):
                for k in range(1, rollMax[j] + 1):
                    if k > 1:
                        dp[i][j][k] = dp[i - 1][j][k - 1]
                    else:
                        for m in range(6):
                            for o in range(1, rollMax[m] + 1):
                                if m != j:
                                    dp[i][j][k] += dp[i - 1][m][o]
        res = 0
        for i in range(6):
            for k in range(1, rollMax[i] + 1):
                res += dp[n - 1][i][k]
        return res % (10**9 + 7)


solution = Solution()

n = 2

rollMax = [1, 1, 2, 2, 2, 3]

assert solution.dieSimulator(n, rollMax) == 34, "Test case 1 failed"

n = 2

rollMax = [1, 1, 1, 1, 1, 1]

assert solution.dieSimulator(n, rollMax) == 30, "Test case 2 failed"

n = 3

rollMax = [1, 1, 1, 2, 2, 3]

assert solution.dieSimulator(n, rollMax) == 181, "Test case 3 failed"

print("PASSED")
