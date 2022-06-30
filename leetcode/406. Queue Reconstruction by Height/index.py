from typing import List


class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        res = []
        people.sort(key = lambda x : (-x[0], x[1]))
        for a in people:
            res.insert(a[1], a)
        return res

solution = Solution()
people = [[7,0],[4,4],[7,1],[5,0],[6,1],[5,2]]
assert solution.reconstructQueue(people) == [[5,0],[7,0],[5,2],[6,1],[4,4],[7,1]], "Should be [[5,0],[7,0],[5,2],[6,1],[4,4],[7,1]]"