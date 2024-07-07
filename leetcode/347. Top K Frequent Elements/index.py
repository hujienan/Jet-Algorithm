from collections import Counter, defaultdict
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c = Counter(nums)
        return [key for key, val in c.most_common(k)]

    def topKFrequent1(self, nums: List[int], k: int) -> List[int]:
        dic = defaultdict(int)
        for num in nums:
            dic[num] += 1
        dic = dic.items()
        dic = sorted(dic, key=lambda x: x[1], reverse=True)
        return [_[0] for _ in dic[:k]]


solution = Solution()
nums = [1, 1, 1, 2, 2, 3]
assert solution.topKFrequent(nums, 2) == [1, 2], "Test case 1 failed"
assert solution.topKFrequent1(nums, 2) == [1, 2], "Test case 1 failed"
nums = [1]
assert solution.topKFrequent(nums, 1) == [1], "Test case 2 failed"
print("All test cases passed")
