from collections import defaultdict
import random
from typing import List


class Solution:

    def __init__(self, nums: List[int]):
        self.dic = defaultdict(list)
        for i in range(len(nums)):
            self.dic[nums[i]].append(i)

    def pick(self, target: int) -> int:
        options = self.dic[target]
        return random.choice(options)


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)

solution = Solution([1, 2, 3, 3, 3])
assert solution.pick(3) in [2, 3, 4], "Test case 1 failed"
assert solution.pick(1) == 0, "Test case 2 failed"
assert solution.pick(2) == 1, "Test case 3 failed"
print("All test cases passed")
