class Solution:
    def findIntegers(self, n: int) -> int:
        bits = 0
        while n >> bits:
            bits += 1
        dp = [0] * (bits+1)
        dp[0] = 1
        dp[1] = 2
        for i in range(2, bits+1):
            dp[i] = dp[i-1] + dp[i-2]
        res = 0
        prev = False
        while bits >= 0:
            mask = 1 << bits
            if mask & n != 0:
                res += dp[bits]
                if prev:
                    return res
                prev = True
            else:
                prev = False
            bits -= 1
        return res+1


solution = Solution()

assert solution.findIntegers(5) == 5, "The result should be 5"

# Here are the non-negative integers <= 5 with their corresponding binary representations:
# 0 : 0
# 1 : 1
# 2 : 10
# 3 : 11
# 4 : 100
# 5 : 101
# Among them, only integer 3 disobeys the rule (two consecutive ones) and the other 5 satisfy the rule.
