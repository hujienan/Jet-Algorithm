class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        left = right = 0
        w = set()
        while left <= right and right < len(s):
            cur = s[right]
            if cur in w:
                w.remove(s[left])
                left += 1
                continue
            w.add(cur)
            right += 1
            res = max(res, right - left)
        return res

solution = Solution()
s = "abcabcbb"
assert solution.lengthOfLongestSubstring(s) == 3, "Should be 3"