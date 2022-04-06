from typing import List


class Solution:
    def grayCode(self, n: int) -> List[int]:
        if n == 1:
            return [0, 1]
        else:
            res = self.grayCode(n-1)
            length = len(res)
            leadingVal = 2 ** (n-1)
            for i in range(length-1, -1, -1):
                res.append(leadingVal + res[i])
            return res
            
solution = Solution()
assert solution.grayCode(2) == [0,1,3,2], "should be [0,1,3,2]"