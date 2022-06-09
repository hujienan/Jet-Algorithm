class Solution:
    def shortestPalindrome(self, s: str) -> str:
        rev = s[::-1]
        length = len(s)
        for i in range(length):
            if s[:length-i] == rev[i:]:
                return rev[:i] + s
        return ""
    def shortestPalindrome1(self, s: str) -> str:
        # KMP
        rev = s[::-1]
        new_s = s + '#' + rev
        length = len(new_s)
        dp = [0] * length
        for i in range(1, length):
            cur = dp[i-1]
            while cur and new_s[cur] != new_s[i]:
                cur = dp[cur-1]
            if new_s[cur] == new_s[i]:
                cur += 1
            dp[i] = cur
        v = dp[length-1]
        return s[v:][::-1] + s

solution = Solution()
res = solution.shortestPalindrome('abaa')
res1 = solution.shortestPalindrome1('abaa')
assert res == 'aabaa', "Should be 'aabaa'"
assert res1 == 'aabaa', "Should be 'aabaa'"