from functools import lru_cache


class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        # recursive way
        if len(s1) + len(s2) != len(s3):
            return False
        @lru_cache(None)
        def bt(a, b, c):
            if not c:
                if not a and not b:
                    return True
                if a or b:
                    return False
            res = False
            c0 = c[0]
            if c0:
                if a and b:
                    if a[0] == c0 and b[0] == c0:
                        res = bt(a[1:], b[:], c[1:]) or bt(a[:], b[1:], c[1:])
                    elif a[0] == c0:
                        res = bt(a[1:], b[:], c[1:])
                    elif b[0] == c0:
                        res = bt(a[:], b[1:], c[1:])
                elif a and not b:
                    if a[0] == c0:
                        res = bt(a[1:], b[:], c[1:])
                elif not a and b:
                    if b[0] == c0:
                        res = bt(a[:], b[1:], c[1:])
            return res
                        
        return bt(s1, s2, s3)


    def isInterleave1(self, s1: str, s2: str, s3: str) -> bool:
        # dp way 2d
        if len(s1) + len(s2) != len(s3):
            return False
        dp = [[False] * (len(s2) + 1) for _ in range(len(s1) + 1)]
        for i in range(len(s1) + 1):
            for j in range(len(s2) + 1):
                if i == 0 and j == 0:
                    dp[i][j] = True
                elif i == 0:
                    dp[i][j] = dp[i][j-1] and s2[j-1] == s3[i+j-1]
                elif j == 0:
                    dp[i][j] = dp[i-1][j] and s1[i-1] == s3[i+j-1]
                else:
                    dp[i][j] = (dp[i-1][j] and s1[i-1] == s3[i+j-1]) or (dp[i][j-1] and s2[j-1] == s3[i+j-1])
        return dp[i][j]
    
    def isInterleave2(self, s1: str, s2: str, s3: str) -> bool:
        # dp way 1d
        if len(s1) + len(s2) != len(s3):
            return False
        dp = [False] * (len(s2) + 1)
        for i in range(len(s1) + 1):
            for j in range(len(s2) + 1):
                if i == 0 and j == 0:
                    dp[j] = True
                elif i == 0:
                    dp[j] = dp[j-1] and s2[j-1] == s3[i+j-1]
                elif j == 0:
                    dp[j] = dp[j] and s1[i-1] == s3[i+j-1]
                else:
                    dp[j] = (dp[j] and s1[i-1] == s3[i+j-1]) or (dp[j-1] and s2[j-1] == s3[i+j-1])
        return dp[j]

solution = Solution()
s1 = "aabcc"
s2 = "dbbca"
s3 = "aadbbcbcac"
assert solution.isInterleave(s1, s2, s3) == True, "Should be True"
assert solution.isInterleave1(s1, s2, s3) == True, "Should be True"
assert solution.isInterleave2(s1, s2, s3) == True, "Should be True"
