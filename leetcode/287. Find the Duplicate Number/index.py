from typing import List


class Solution:
    def findDuplicate1(self, nums: List[int]) -> int:
        sum1 = sum(nums)
        setNums = set(nums)
        sum2 = sum(setNums)
        return (sum1 - sum2) // (len(nums) - len(setNums)) 
    
    def findDuplicate2(self, nums: List[int]) -> int:
        
        tortoise = hare = nums[0]
        while True:
            tortoise = nums[tortoise]
            hare = nums[nums[hare]]
            if tortoise == hare:
                break
        tortoise = nums[0]
        while tortoise != hare:
            tortoise = nums[tortoise]
            hare = nums[hare]
            
        return hare

solution = Solution()
nums = [1,3,4,2,2]
assert solution.findDuplicate1(nums) == 2, "Should be 2"
assert solution.findDuplicate2(nums) == 2, "Should be 2"

        