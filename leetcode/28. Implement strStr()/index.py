class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        m = len(haystack)
        n = len(needle)
        if n == 1 and needle[0] == haystack[0]:
            return 0
        sufix = [0] * n
        for i in range(1, n):
            cur = sufix[i - 1]
            while cur and needle[cur] != needle[i]:
                cur = sufix[cur-1]
            if needle[cur] == needle[i]:
                cur += 1
            sufix[i] = cur
        dp = [0] * m
        if haystack[0] == needle[0]:
            dp[0] = 1
        for i in range(1, m):
            cur = dp[i - 1]
            while cur and haystack[i] != needle[cur]:
                cur = sufix[cur - 1]
            if haystack[i] == needle[cur]:
                cur += 1
            if cur == n:
                return i - n + 1
            dp[i] = cur
        return -1

solution = Solution()
haystack = "hello"
needle = "ll"
assert solution.strStr(haystack, needle) == 2, "Should be 2"