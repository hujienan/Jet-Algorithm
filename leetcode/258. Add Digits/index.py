class Solution:
    def addDigits(self, num: int) -> int:
        # def dp(s):
        #     if len(s) == 1:
        #         return int(s)
        #     list_s = list(s)
        #     acc = 0
        #     for n in list_s:
        #         acc += int(n)
        #     return dp(str(acc))
        # return dp(str(num))
        if num == 0:
            return 0
        if num % 9 == 0:
            return 9
        return num % 9


solution = Solution()
assert solution.addDigits(38) == 2, "Should be 2"
