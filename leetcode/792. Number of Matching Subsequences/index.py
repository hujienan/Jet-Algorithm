from typing import List


class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        def check(word):
            pos = -1
            for c in word:
                pos = s.find(c, pos+1)
                if pos == -1:
                    return False
            return True
        return sum(map(check, words))

solution = Solution()
s = "abcde"
words = ["a","bb","acd","ace"]
assert solution.numMatchingSubseq(s, words) == 3, "Should be 3"