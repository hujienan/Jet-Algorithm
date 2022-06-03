class Solution:
    def longestPrefix(self, s: str) -> str:
        dp = [0] * len(s)
        for i in range(1, len(s)):
            c = dp[i-1]
            while c and s[c] != s[i]:
                c = dp[c-1]
            if s[c] == s[i]:
                c += 1
            dp[i] = c
        l = dp[len(s)-1]
        return s[:l]
            
solution = Solution()
s = "level"
assert solution.longestPrefix(s) == 'l', "Should be 'l'"