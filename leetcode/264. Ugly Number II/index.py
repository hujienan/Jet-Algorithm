class Solution:
    def nthUglyNumber(self, n: int) -> int:
        l = [1]
        # current indexes
        l1 = l2 = l3 = 0
        while len(l) < n:
            i1 = 2 * l[l1]
            i2 = 3 * l[l2]
            i3 = 5 * l[l3]
            i = min(i1, i2, i3)
            # find the min
            l.append(i)
            # move the index respectively
            if i == i1:
                l1 += 1
            if i == i2:
                l2 += 1
            if i == i3:
                l3 += 1
        return l[-1]
            
solution = Solution()
n = 10
assert solution.nthUglyNumber(n) == 12, "Should be 12"
        