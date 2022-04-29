from collections import defaultdict


class Solution:
    def maximumSwap(self, num: int) -> int:
        nums = list(str(num))
        dic = defaultdict(list)
        for i in range(len(nums)):
            dic[nums[i]].append(i)
        sortedNums = sorted(set(nums), reverse=True)
        for n in sortedNums:
            for i in sorted(dic[n], reverse=True):
                start = 0
                while start < i:
                    if nums[start] < n:
                        nums[start], nums[i] = nums[i], nums[start]
                        return int(''.join(nums))
                    start += 1
        return int(''.join(nums))

solution = Solution()
num = 2736
assert solution.maximumSwap(num) == 7236, "Should be 7236"