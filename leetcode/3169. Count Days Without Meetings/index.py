from typing import List


class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        meetings.sort()
        last_end = 0
        res = 0
        for start, end in meetings:
            if start > last_end:
                res += start - last_end - 1
            last_end = max(last_end, end)
        res += days - last_end
        return res


solution = Solution()
days = 57
meetings = [[3, 49], [23, 44], [21, 56], [26, 55], [23, 52], [2, 9], [1, 48], [3, 31]]
assert solution.countDays(days, meetings) == 1, "Failed"
