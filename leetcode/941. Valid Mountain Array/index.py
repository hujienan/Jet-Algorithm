from typing import List


class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr) < 3:
            return False
        
        flag = True
        incre = False
        for i in range(len(arr)):
            if i == 0:
                continue
            if flag:
                if arr[i] < arr[i-1]:
                    flag = False
                if arr[i] == arr[i-1]:
                    return False
                if arr[i] > arr[i-1]:
                    incre = True
            else:
                if arr[i] >= arr[i-1]:
                    return False
                
        return True if not flag and incre else False

solution = Solution()
assert solution.validMountainArray([3,5,5]) == False, "Should be false"