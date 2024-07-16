class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        l = [_ for _ in range(1, n + 1)]
        start = 0
        while len(l) > 1:
            next_out = (start + k - 1) % len(l)
            l.pop(next_out)
            start = next_out
        return l[0]
