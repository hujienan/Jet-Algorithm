from math import inf
from typing import List


class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        dic = {}
        res = [inf, {}]
        for i in range(len(list1)):
            dic[list1[i]] = i
        for i in range(len(list2)):
            if list2[i] in dic:
                index_sum = i + dic[list2[i]]
                if index_sum < res[0]:
                    res = [index_sum, {list2[i]}]
                elif index_sum == res[0]:
                    res[1].add(list2[i])
        return list(res[1])

solution = Solution()
list1 = ["Shogun","Tapioca Express","Burger King","KFC"]
list2 = ["Piatti","The Grill at Torrey Pines","Hungry Hunter Steakhouse","Shogun"]
assert solution.findRestaurant(list1, list2) == ["Shogun"], "Should be ['Shogun']"