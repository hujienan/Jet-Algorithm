class Solution:
    def bitwiseComplement(self, n: int) -> int: 
        return 1 if n == 0 else n ^ int('1' * (n).bit_length(), 2)

solution = Solution()
assert solution.bitwiseComplement(5) == 2, "Should be 2"