class Solution:
    def smallestNumber(self, num: int) -> int:
        if num > 0:
            nums = sorted(list(str(num)))
            if nums[0] == '0':
                cur = 1
                while nums[cur] == '0':
                    cur += 1
                nums[0], nums[cur] = nums[cur], nums[0]
            return int("".join(nums))
        if num == 0:
            return 0
        num = -num
        nums = sorted(list(str(num)), reverse=True)
        return -int("".join(nums))

solution = Solution()
num = 310
assert solution.smallestNumber(num) == 103, "Should be 103"