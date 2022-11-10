from typing import List


class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        arr = sorted(arr)
        gap = arr[1] - arr[0]
        for i in range(2, len(arr)):
            if arr[i] - arr[i-1] != gap:
                return False
        return True

solution = Solution()
arr = [3,5,1]
assert solution.canMakeArithmeticProgression(arr) == True, "Should be true"