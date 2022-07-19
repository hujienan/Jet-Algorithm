from typing import List


class Solution:
    def maximumNumber(self, num: str, change: List[int]) -> str:
        nums = [int(_) for _ in num]
        i = 0
        mutate = False
        while i < len(nums):
            if not mutate:
                if nums[i] < change[nums[i]]:
                    nums[i] = change[nums[i]]
                    mutate = True
            else:
                if nums[i] <= change[nums[i]]:
                    nums[i] = change[nums[i]]
                else:
                    break
            i += 1
        return "".join(str(_) for _ in nums)

solution = Solution()
num = "132"
change = [9,8,5,0,3,6,4,2,6,8]
assert solution.maximumNumber(num, change) == "832", "Should be 832"