from typing import List


class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        a = list(allowed)
        res = 0
        for word in words:
            for c in word:
                if c not in a:
                    break
            else:
                res += 1
        return res

solution = Solution()
allowed = "ab"
words = ["ad","bd","aaab","baa","badab"]
assert solution.countConsistentStrings(allowed, words) == 2, "Should be 2"