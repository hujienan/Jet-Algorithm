from functools import lru_cache


class Solution:
    @lru_cache(None)
    def isScramble(self, s1: str, s2: str) -> bool:
        if s1 == s2:
            return True
        if sorted(s1) != sorted(s2):
            return False
        for i in range(1, len(s1)):
            if self.isScramble(s1[:i], s2[:i]) and self.isScramble(s1[i:], s2[i:]):
                return True
            if self.isScramble(s1[:i], s2[len(s2)-i:]) and self.isScramble(s1[i:], s2[:len(s2)-i]):
                return True
        return False

solution = Solution()
s1 = "eebaacbcbcadaaedceaaacadccd"
s2 = "eadcaacabaddaceacbceaabeccd"
assert solution.isScramble(s1, s2) == False, "Should be false"