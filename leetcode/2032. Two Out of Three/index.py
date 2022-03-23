from collections import Counter
from typing import List


class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        set_1, set_2, set_3 = set(nums1), set(nums2), set(nums3)
        c = Counter(set_1) + Counter(set_2) + Counter(set_3)
        return [_ for _ in c if c[_] >= 2]
        
solution = Solution()
nums1 = [1,1,3,2]
nums2 = [2,3]
nums3 = [3]
assert solution.twoOutOfThree(nums1, nums2, nums3) == [2,3], "Should be [2,3]"