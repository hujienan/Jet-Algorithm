from typing import List


class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        res = 0
        if n <= 0:
            return True
        length = len(flowerbed)
        for i in range(length):
            if (i - 1 < 0 or flowerbed[i-1] == 0) and (i + 1 >= length or flowerbed[i+1] == 0) and flowerbed[i] == 0:
                flowerbed[i] = 1
                res += 1
                if (res >= n):
                    return True
        return False


solution = Solution()
assert solution.canPlaceFlowers([1, 0, 0, 0, 1], 1) == True, "Should be true"
