from typing import List


class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        gap = arr[1] - arr[0]
        for i in range(2, len(arr)):
            gap = min(gap, arr[i] - arr[i-1])
        res = []
        i = 1
        while i < len(arr):
            if arr[i] - arr[i-1] == gap:
                res.append([arr[i-1], arr[i]])
            i += 1
        return res

solution = Solution()
arr = [4,2,1,3]
assert solution.minimumAbsDifference(arr) == [[1,2],[2,3],[3,4]], "Should be [[1,2],[2,3],[3,4]]"