class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        def t(n):
            if n < numExchange:
                return 0
            full, empty = divmod(n, numExchange)
            return full + t(full + empty)

        return numBottles + t(numBottles)


solution = Solution()
numBottles = 9
numExchange = 3
assert solution.numWaterBottles(numBottles, numExchange) == 13, "Test case 1 failed"
numBottles = 15
numExchange = 4
assert solution.numWaterBottles(numBottles, numExchange) == 19, "Test case 2 failed"
