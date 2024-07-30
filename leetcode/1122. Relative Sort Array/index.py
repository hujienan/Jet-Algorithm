from collections import defaultdict


class Solution:
    def relativeSortArray(self, arr1: list[int], arr2: list[int]) -> list[int]:
        dic = defaultdict(int)
        arr2_set = set(arr2)
        end = []
        for num in arr1:
            if num not in arr2_set:
                end.append(num)
            dic[num] += 1
        end.sort()
        res = []
        for num in arr2:
            for _ in range(dic[num]):
                res.append(num)
        return res + end


solution = Solution()

arr1 = [2, 3, 1, 3, 2, 4, 6, 7, 9, 2, 19]

arr2 = [2, 1, 4, 3, 9, 6]

assert solution.relativeSortArray(arr1, arr2) == [
    2,
    2,
    2,
    1,
    4,
    3,
    3,
    9,
    6,
    7,
    19,
], "Test case 1 failed"


arr1 = [28, 6, 22, 8, 44, 17]

arr2 = [22, 28, 8, 6]

assert solution.relativeSortArray(arr1, arr2) == [
    22,
    28,
    8,
    6,
    17,
    44,
], "Test case 2 failed"

print("PASSED")
