from typing import List


class Solution:
    def maxNumber(self, nums1: List[int], nums2: List[int], k: int) -> List[int]:
                
        def findMaxInNums(nums, i):
            stack = []
            drop = len(nums) - i
            for num in nums:
                while stack and stack[-1] < num and drop:
                    stack.pop()
                    drop -= 1
                stack.append(num)
            return stack[:i]
        def getMergedMax(nums1, nums2):
            return [max(nums1, nums2).pop(0) for _ in nums1 + nums2]

        res = [0]
        for i in range(k+1):
            j = k - i
            if i <= len(nums1) and j <= len(nums2):
                maxInNums1 = findMaxInNums(nums1, i)
                maxInNums2 = findMaxInNums(nums2, j)
                mergedMax = getMergedMax(maxInNums1, maxInNums2)
                cur = int(''.join([str(_) for _ in res]))
                if int(''.join([str(_) for _ in mergedMax])) > cur:
                    res = mergedMax
        return res

solution = Solution()
nums1 = [6,7]
nums2 = [6,0,4]
k = 5
assert solution.maxNumber(nums1, nums2, k) == [6,7,6,0,4], "Should be [6,7,6,0,4]"