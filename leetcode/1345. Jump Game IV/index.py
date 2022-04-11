from collections import defaultdict, deque
from typing import List


class Solution:
    def minJumps(self, arr: List[int]) -> int:
        dic = defaultdict(list)
        length = len(arr)
        for i in range(length):
            dic[arr[i]].append(i)
        q = deque([[0, 0]])
        visited = set()
        
        while True:
            cur_index, cur_step = q.popleft()
            if cur_index == length - 1:
                return cur_step
            visited.add(cur_index)
            if cur_index + 1 < length and (cur_index + 1) not in visited:
                q.append([cur_index + 1, cur_step + 1])
            if cur_index - 1 >= 0 and (cur_index - 1) not in visited:
                q.append([cur_index - 1, cur_step + 1])
            for same_i in dic[arr[cur_index]]:
                if same_i not in visited:
                    q.append([same_i, cur_step + 1])
            dic[arr[cur_index]].clear()
            
solution = Solution()
arr = [100,-23,-23,404,100,23,23,23,3,404]
assert solution.minJumps(arr) == 3, "Should be 3"