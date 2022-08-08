from math import ceil, log


class Solution:
    def poorPigs(self, buckets: int, minutesToDie: int, minutesToTest: int) -> int:
        t = minutesToTest // minutesToDie + 1
        # t^number_of_pigs >= buckets
        # so number of pigs = ceil(log(buckets, t))
        return ceil(log(buckets, t))

solution = Solution()
buckets = 1000
minutesToDie = 15
minutesToTest = 60
assert solution.poorPigs(buckets, minutesToDie, minutesToTest) == 5, "Should be 5"