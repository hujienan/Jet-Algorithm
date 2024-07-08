class Solution:
    def longestPalindrome(self, s: str) -> str:
        def expand(l, r):
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            return s[l + 1 : r]

        res = ""
        for i in range(len(s)):
            res = max(res, expand(i, i), expand(i, i + 1), key=len)
        return res


solution = Solution()
s = "babad"
assert solution.longestPalindrome(s) == "bab", "Should be bab"
s = "cbbd"
assert solution.longestPalindrome(s) == "bb", "Should be bb"
s = "a"
assert solution.longestPalindrome(s) == "a", "Should be a"
s = "ac"
assert solution.longestPalindrome(s) == "a", "Should be a"
print("All test cases passed")
