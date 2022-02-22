class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        chars = list(columnTitle)
        chars.reverse()
        length = len(chars)
        res = 0
        for i in range(length):
            val = ord(chars[i]) - 64
            res += (val * pow(26, i))
        return res


solution = Solution()
assert solution.titleToNumber('AB') == 28, "Should be 28"
