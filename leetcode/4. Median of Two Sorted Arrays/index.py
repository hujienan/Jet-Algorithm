from cmath import inf
from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        a, b = nums1, nums2
        total_length = len(a) + len(b)
        half_length = total_length // 2
        if len(a) > len(b):
            a, b = b, a
        left, right = 0, len(a) - 1
        while True:
            i = (left + right) // 2
            j = half_length - (i + 1) - 1
            a_left = a[i] if i >= 0 else -inf
            a_right = a[i+1] if (i + 1) < len(a) else inf
            b_left = b[j] if j >= 0 else -inf
            b_right = b[j + 1] if (j + 1) < len(b) else inf
            if a_left <= b_right and b_left <= a_right:
                if total_length % 2:
                    return min(a_right, b_right)
                return (max(a_left, b_left) + min(a_right, b_right)) / 2
            elif a_left > b_right:
                right = i - 1
            else:
                left = i + 1

solution = Solution()
nums1 = [1,2]
nums2 = [3,4]
assert solution.findMedianSortedArrays(nums1, nums2) == 2.5, "Should be 2.5"
            