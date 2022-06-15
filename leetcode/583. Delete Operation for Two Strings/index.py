from functools import lru_cache


class Solution:
    def minDistance1(self, word1: str, word2: str) -> int:
        # recursive way
        @lru_cache(None)
        def lcs(s1, s2, i, j):
            if i == len(s1) or j == len(s2):
                return 0
            if s1[i] == s2[j]:
                return 1 + lcs(s1, s2, i + 1, j + 1)
            return max(lcs(s1, s2, i + 1, j), lcs(s1, s2, i, j + 1))
        return len(word1) + len(word2) - 2 * lcs(word1, word2, 0, 0)
    
    def minDistance2(self, word1: str, word2: str) -> int:
        # dp way with lcs
        m ,n = len(word1), len(word2)
        dp = [[0 for _ in range(n+1)] for _ in range(m+1)]
        for i in range(1, m+1):
            for j in range(1, n+1):
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = 1 + dp[i-1][j-1]
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        return m + n - 2 * dp[m][n]

    def minDistance3(self, word1: str, word2: str) -> int:
        # 2-d dp without lcs
        m, n = len(word1), len(word2)
        dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
        for i in range(m + 1):
            for j in range(n + 1):
                if i == 0 or j == 0:
                    dp[i][j] = i + j
                elif word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = 1 + min(dp[i - 1][j], dp[i][j - 1])
        return dp[m][n]

    def minDistance4(self, word1: str, word2: str) -> int:
        # 1-d dp without lcs
        n = len(word2)
        dp = [0] * (n + 1)
        for i in range(len(word1) + 1):
            temp = [0] * (n + 1)
            for j in range(n + 1):
                if i == 0 or j == 0:
                    temp[j] = i + j
                elif word1[i-1] == word2[j-1]:
                    temp[j] = dp[j - 1]
                else:
                    temp[j] = 1 + min(dp[j], temp[j-1])
            dp = temp
        return dp[n]

solution = Solution()
s1 = 'abc'
s2 = 'bca'
assert solution.minDistance1(s1, s2) == 2, "Should be 2"
assert solution.minDistance2(s1, s2) == 2, "Should be 2"
assert solution.minDistance3(s1, s2) == 2, "Should be 2"
assert solution.minDistance4(s1, s2) == 2, "Should be 2"