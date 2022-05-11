from typing import List


class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        res = []
        length = len(s)
        if length < 4:
            return res
        def bt(s, comb = []):
            if len(comb) == 4:
                if not s:
                    cur = ".".join(comb)  
                    if cur not in res:
                        res.append(cur)
                return
            if not s:
                return
            for l in range(1, 4):
                if s[0] == '0' and l > 1:
                    return
                if int(s[:l]) > 255:
                    return
                comb.append(s[:l])
                bt(s[l:], comb[:])
                comb.pop()
        bt(s)
        return res
        
solution = Solution()
s = "101023"
assert solution.restoreIpAddresses(s) == ["1.0.10.23","1.0.102.3","10.1.0.23","10.10.2.3","101.0.2.3"], """Should be ["1.0.10.23","1.0.102.3","10.1.0.23","10.10.2.3","101.0.2.3"] """