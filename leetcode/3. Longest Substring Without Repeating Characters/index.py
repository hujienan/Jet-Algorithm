class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        left, right = 0, 0
        w = []
        while left <= right and right < len(s):
            if not s[right] in w:
                w.append(s[right])
                right += 1
                res = max(res, right - left)
            else:
                w.remove(s[left])
                left += 1
                res = max(res, right - left)
        return res

solution = Solution()
s = "abcabcbb"
assert solution.lengthOfLongestSubstring(s) == 3, "Should be 3"