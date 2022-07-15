from math import gcd


class Solution:
    def nthUglyNumber(self, n: int, a: int, b: int, c: int) -> int:
        lcm_ab = a * b // gcd(a, b)
        lcm_bc = b * c // gcd(b, c)
        lcm_ac = a * c // gcd(a, c)
        lcm_abc = lcm_ab * c // gcd(c , lcm_ab)
        left = 1
        right = 10 ** 10
        while left < right:
            mid = left + (right - left) // 2
            count = mid // a + mid // b + mid // c - mid // lcm_ab - mid // lcm_ac - mid // lcm_bc + mid // lcm_abc
            if count >= n:
                right = mid
            else:
                left = mid + 1
        return left
            
solution = Solution()
n = 3
a = 2
b = 3
c = 5
assert solution.nthUglyNumber(n, a, b, c) == 4, "Should be 4"