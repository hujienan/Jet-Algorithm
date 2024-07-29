class Solution:
    def threeConsecutiveOdds(self, arr: list[int]) -> bool:
        window = 0
        for i in arr:
            if i % 2 == 1:
                window += 1
                if window == 3:
                    return True
            else:
                window = 0
        return False


solution = Solution()

arr = [2, 6, 4, 1]

assert not solution.threeConsecutiveOdds(arr), "Should be False"

arr = [1, 2, 34, 3, 4, 5, 7, 23, 12]

assert solution.threeConsecutiveOdds(arr), "Should be True"


print("PASSED")
