from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # dp
        dp = [1] * len(nums)
        for i in range(len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], 1 + dp[j])
        return max(dp)

    def lengthOfLIS1(self, nums: List[int]) -> int:
        # binary search
        piles = []
        for num in nums:
            left = 0
            right = len(piles)
            while left < right:
                mid = (left + right) // 2
                if piles[mid] > num:
                    right = mid
                elif piles[mid] < num:
                    left = mid + 1
                else:
                    right = mid
            if left == len(piles):
                piles.append(num)
            else:
                piles[left] = num
        return len(piles)

solution = Solution()
nums = [10,9,2,5,3,7,101,18]
assert solution.lengthOfLIS(nums) == 4, "Should be 4"
assert solution.lengthOfLIS1(nums) == 4, "Should be 4"
        
        