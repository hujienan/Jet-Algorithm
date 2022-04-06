from typing import List


class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        bits.pop()
        i = 0
        while i < len(bits):
            if bits[i] == 0:
                i += 1
            else:
                i += 2
        return i == len(bits)

solution = Solution()
bits = [1,1,1,0]
assert solution.isOneBitCharacter(bits) == False, "Should be false"