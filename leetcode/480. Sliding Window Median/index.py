from bisect import insort
from typing import List


class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        window = sorted(nums[:k])
        res = []
        if k % 2:
            res.append(window[k // 2])
        else:
            res.append((window[k // 2] + window[(k // 2 - 1)]) / 2)
        left = 0
        right = k
        length = len(nums)
        while right < length:
            window.remove(nums[left])
            insort(window, nums[right])
            if k % 2:
                res.append(window[k // 2])
            else:
                res.append((window[k // 2] + window[(k // 2 - 1)]) / 2)
            right += 1
            left += 1
        return res

solution = Solution()
nums = [1,3,-1,-3,5,3,6,7]
k = 3
assert solution.medianSlidingWindow(nums, k) == [1.00000,-1.00000,-1.00000,3.00000,5.00000,6.00000], "Should be [1.00000,-1.00000,-1.00000,3.00000,5.00000,6.00000]"