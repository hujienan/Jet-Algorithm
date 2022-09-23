class Solution:
    def concatenatedBinary(self, n: int) -> int:
        return int("".join(bin(_)[2:] for _ in range(1, n+1)), 2) % (10**9 + 7)

solution = Solution()
n = 12
assert solution.concatenatedBinary(n) == 505379714, "Should be 505379714"