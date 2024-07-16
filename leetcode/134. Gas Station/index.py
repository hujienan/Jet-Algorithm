from typing import List


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
        fuel = 0
        start = 0
        for i in range(len(gas)):
            fuel += gas[i] - cost[i]
            if fuel < 0:
                fuel = 0
                start = i + 1
        return start


solution = Solution()

gas = [1, 2, 3, 4, 5]
cost = [3, 4, 5, 1, 2]
assert solution.canCompleteCircuit(gas, cost) == 3, "Should be 3"
