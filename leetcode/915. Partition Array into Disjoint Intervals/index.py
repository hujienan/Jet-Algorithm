class Solution:
    def partitionDisjoint1(self, nums: list[int]) -> int:
        # basic approach
        n = len(nums)
        max_left = [0] * n
        min_right = [0] * n

        max_left[0] = nums[0]
        for i in range(1, n):
            max_left[i] = max(nums[i], max_left[i-1])
        
        min_right[-1] = nums[-1]
        for i in range(n-2, -1, -1):
            min_right[i] = min(min_right[i+1], nums[i])
        
        for i in range(1, n):
            if max_left[i] <= min_right[i+1]:
                return i + 1
    def partitionDisjoint2(self, nums: list[int]) -> int:
        # 2 rounds approach
        n = len(nums)
        min_right = [0] * n
        min_right[-1] = nums[-1]
        for i in range(n-2, -1, -1):
            min_right[i] = min(nums[i], min_right[i+1])
        cur_max = nums[0]
        for i in range(1, n):
            if cur_max <= min_right[i]:
                return i
            cur_max = max(cur_max, nums[i])

    def partitionDisjoint3(self, nums: list[int]) -> int:
        # 1 round
        n = len(nums)
        left_max = global_max = nums[0]
        pos = 0
        for i in range(1, n):
            global_max = max(global_max, nums[i])
            if nums[i] < left_max:
                # move pos forward
                pos = i
                left_max = global_max
        return pos+1

solution = Solution()
res = solution.partitionDisjoint3([32,57,24,19,0,24,49,67,87,87])
assert res == 7, "[32,57,24,19,0,24,49], [67,87,87]"
