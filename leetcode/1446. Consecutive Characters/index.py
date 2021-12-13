class Solution:
    def maxPower(self, s: str) -> int:
        last = ""
        res = 0
        length = 0
        for c in s:
            if c != last:
                last = c
                length = 1
            else:
                length += 1
            res = max(res, length)
        return res


solution = Solution()
assert solution.maxPower("abbcccddddeeeeedcba") == 5, "Should be 5"
