from collections import defaultdict
from typing import List


class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        loses = defaultdict(int)
        players = set()
        for winner, loser in matches:
            loses[loser] += 1
            players.add(winner)
            players.add(loser)
        res1 = []
        res2 = []
        for player in players:
            if loses[player] == 0:
                res1.append(player)
            if loses[player] == 1:
                res2.append(player)
        return [sorted(res1), sorted(res2)]

solution = Solution()
matches = [[1,3],[2,3],[3,6],[5,6],[5,7],[4,5],[4,8],[4,9],[10,4],[10,9]]
assert solution.findWinners(matches) == [[1,2,10],[4,5,7,8]], "Should be [[1,2,10],[4,5,7,8]]"