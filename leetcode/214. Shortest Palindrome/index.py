class Solution:
    def shortestPalindrome(self, s: str) -> str:
        rev = s[::-1]
        length = len(s)
        for i in range(length):
            if s[:length-i] == rev[i:]:
                return rev[:i] + s
        return ""

solution = Solution()
res = solution.shortestPalindrome('abaa')
assert res == 'aabaa', "Should be 'aabaa'"