from typing import List


class LargerNumKey(str):
    def __lt__(x, y):
        return x+y > y+x

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        largest_num = "".join(sorted(map(str, nums), key=LargerNumKey))
        return '0' if largest_num[0] == '0' else largest_num 

solution = Solution()
nums = [10,2]
assert solution.largestNumber(nums) == "210", "should be 210"