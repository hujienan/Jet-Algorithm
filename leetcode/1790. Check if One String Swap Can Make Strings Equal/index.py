class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        if len(s1) != len(s2):
            return False
        if s1 == s2:
            return True
        diffs = [i for i in range(len(s1)) if s1[i] != s2[i]]
        if len(diffs) != 2:
            return False
        s1 = list(s1)
        s1[diffs[0]], s1[diffs[1]] = s1[diffs[1]], s1[diffs[0]]
        return "".join(s1) == s2

solution = Solution()
s1 = "bank"
s2 = "kanb"
assert solution.areAlmostEqual(s1, s2) == True, "Should be true"