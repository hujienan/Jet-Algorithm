class Solution:
    # Recursion with Memoization
    def findTargetSumWays1(self, nums: list[int], target: int) -> int:
        memo = {}

        def recur(i, total):
            if i == len(nums):
                if total == target:
                    return 1
                return 0
            if (i, total) in memo:
                return memo[(i, total)]
            res = recur(i+1, total + nums[i]) + recur(i+1, total - nums[i])
            memo[(i, total)] = res
            return memo[(i, total)]
        return recur(0, 0)
    # 2D Dynamic Programming

    def findTargetSumWays2(self, nums: list[int], target: int) -> int:
        dp = [[0] * 2001 for _ in range(len(nums))]
        dp[0][nums[0]+1000] = 1
        dp[0][-nums[0]+1000] += 1
        for i in range(1, len(nums)):
            for total in range(2001):
                if dp[i-1][total] > 0:
                    dp[i][total+nums[i]] += dp[i-1][total]
                    dp[i][total-nums[i]] += dp[i-1][total]
        return dp[len(nums)-1][target+1000]
    # 1D Dynamic Programming

    def findTargetSumWays3(self, nums: list[int], target: int) -> int:
        dp = [0] * 2001
        dp[nums[0] + 1000] = 1
        dp[-nums[0] + 1000] += 1
        for i in range(1, len(nums)):
            temp = [0] * 2001
            for total in range(2001):
                if dp[total] > 0:
                    temp[total+nums[i]] += dp[total]
                    temp[total-nums[i]] += dp[total]
            dp = temp
        return dp[target+1000]
    # Math trick

    def findTargetSumWays4(self, nums: list[int], target: int) -> int:
        total = sum(nums)
        if (total + target) % 2 or total < target:
            return 0
        cal = (total + target) // 2
        dp = [0] * (cal + 1)
        dp[0] = 1
        for num in nums:
            for j in range(cal, num-1, -1):
                dp[j] += dp[j-num]
        return dp[cal]

solution = Solution()
nums = [1,1,1,1,1]
target = 3
assert solution.findTargetSumWays1(nums, target) == 5, "Should be 5"
assert solution.findTargetSumWays2(nums, target) == 5, "Should be 5"
assert solution.findTargetSumWays3(nums, target) == 5, "Should be 5"
assert solution.findTargetSumWays4(nums, target) == 5, "Should be 5"