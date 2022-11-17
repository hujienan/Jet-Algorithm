from typing import List


class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        overlap_x = min(rec2[2], rec1[2]) - max(rec2[0], rec1[0])
        overlap_y = min(rec2[3], rec1[3]) - max(rec2[1], rec1[1])
        if overlap_x > 0 and overlap_y > 0:
            return True
        return False

solution = Solution()
rec1 = [0,0,2,2]
rec2 = [1,1,3,3]
assert solution.isRectangleOverlap(rec1, rec2) == True, "Should be True"