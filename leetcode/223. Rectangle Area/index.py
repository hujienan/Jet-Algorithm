class Solution:
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:
        total = (ax2 - ax1) * (ay2 - ay1) + (bx2 - bx1) * (by2 - by1)
        overlap_x = min(ax2, bx2) - max(bx1, ax1)
        overlap_y = min(ay2, by2) - max(ay1, by1)
        if overlap_x > 0 and overlap_y > 0:
            return total - overlap_x * overlap_y
        return total


solution = Solution()
ax1 = -3
ay1 = 0
ax2 = 3
ay2 = 4
bx1 = 0
by1 = -1
bx2 = 9
by2 = 2
assert solution.computeArea(ax1, ay1, ax2, ay2, bx1, by1, bx2, by2) == 45, "Should be 45"