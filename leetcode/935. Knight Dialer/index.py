class Solution:
    def knightDialer(self, n: int) -> int:
        arr = [1] * 10
        for i in range(n - 1):
            arr = [
                arr[4] + arr[6],
                arr[6] + arr[8],
                arr[7] + arr[9],
                arr[4] + arr[8],
                arr[0] + arr[3] + arr[9],
                0,
                arr[0] + arr[1] + arr[7],
                arr[2] + arr[6],
                arr[1] + arr[3],
                arr[2] + arr[4],
            ]
        return sum(arr) % (pow(10, 9) + 7)


solution = Solution()
assert solution.knightDialer(1) == 10, "Should be 10"
assert solution.knightDialer(2) == 20, "Should be 20"
assert solution.knightDialer(3131) == 136006598, "Should be 136006598"
