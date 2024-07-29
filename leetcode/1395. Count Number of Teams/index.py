class Solution:
    def numTeams(self, rating: list[int]) -> int:
        res = 0
        for i in range(1, len(rating) - 1):
            num = rating[i]
            left = rating[:i]
            right = rating[i + 1 :]
            left_less_nums = len([_ for _ in left if _ < num])
            left_greater_nums = len(left) - left_less_nums
            right_less_nums = len([_ for _ in right if _ < num])
            right_greater_nums = len(right) - right_less_nums
            res += left_less_nums * right_greater_nums
            res += left_greater_nums * right_less_nums
        return res


solution = Solution()

rating = [2, 5, 3, 4, 1]
assert solution.numTeams(rating) == 3, "Should be 3"

rating = [2, 1, 3]
assert solution.numTeams(rating) == 0, "Should be 0"

rating = [1, 2, 3, 4]

assert solution.numTeams(rating) == 4, "Should be 4"

print("PASSED")
