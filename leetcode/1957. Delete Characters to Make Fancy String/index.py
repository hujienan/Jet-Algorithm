class Solution:
    def makeFancyString(self, s: str) -> str:
        res = s[0]
        cur = 1
        for i in range(1, len(s)):
            if s[i] == s[i-1]:
                cur += 1
            else:
                cur = 1
            if cur < 3:
                res += s[i]
        return res

solution = Solution()
assert solution.makeFancyString("leeetcode") == "leetcode", "Should be leetcode"