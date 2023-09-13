from collections import Counter


class Solution:
    def minDeletions(self, s: str) -> int:
        c = Counter(s)
        deletions = 0
        freqs = set()
        for char, freq in c.items():
            while freq > 0 and freq in freqs:
                deletions += 1
                freq -= 1
            freqs.add(freq)
        return deletions


solution = Solution()
s = "aaabbbcc"
assert solution.minDeletions(s) == 2
