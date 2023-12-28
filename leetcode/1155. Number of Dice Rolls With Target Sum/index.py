from functools import cache


class Solution:
    @cache
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        if n == 0 and target == 0:
            return 1
        if n == 0 or target <= 0:
            return 0
        return sum(
            [self.numRollsToTarget(n - 1, k, target - _) for _ in range(1, k + 1)]
        ) % (10**9 + 7)


solution = Solution()
n = 30
k = 30
target = 500
assert solution.numRollsToTarget(n, k, target) == 222616187
