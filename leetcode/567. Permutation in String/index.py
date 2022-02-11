from collections import Counter


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        c, w, match = Counter(s1), len(s1), 0
        for i in range(len(s2)):
            if s2[i] in c:
                if not c[s2[i]]:
                    match -= 1
                c[s2[i]] -= 1
                if not c[s2[i]]:
                    match += 1
            if i >= w and s2[i-w] in c:
                if not c[s2[i-w]]:
                    match -= 1
                c[s2[i-w]] += 1
                if not c[s2[i-w]]:
                    match += 1
            if match == len(c):
                return True
        return False

solution = Solution()
assert solution.checkInclusion("ab", "eidbaooo") == True, "Should be true"