class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        res = ""
        while columnNumber:
            columnNumber -= 1
            charValue = columnNumber % 26
            char = chr(charValue + ord('A'))
            res = char + res
            columnNumber //= 26
        return res

solution = Solution()
assert solution.convertToTitle(701) == 'ZY', "Should be 'ZY'"