from collections import Counter
from typing import List


class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        return len(set(Counter(arr).values())) == len(set(arr))
        
solution = Solution()
arr = [1,2,2,1,1,3]
assert solution.uniqueOccurrences(arr) == True, "Should be True"