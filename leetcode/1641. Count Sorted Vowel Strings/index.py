from functools import lru_cache


class Solution:
    def countVowelStrings(self, n: int) -> int:
        @lru_cache(None)
        def c(i, number):
            if i == n:
                return number
            return sum([c(i + 1, _) for _ in range(1, number + 1)])
        return c(1, 5)

        # arr = [1, 1, 1, 1, 1]  ## initial 
        # for i in range(2, n+1):   ## for different values of n
        #     for j in range(5):   ## for 5 vowels
        #         arr[j] = sum(arr[j:])
        # return sum(arr)    ## return sum
        
solution = Solution()
assert solution.countVowelStrings(33) == 66045, "Should be 66045"