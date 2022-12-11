from heapq import heappop, heappush


class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        heap = []
        for count, char in [(-a, 'a'), (-b, 'b'), (-c, 'c')]:
            if count:
                heappush(heap, (count, char))
        res = ""
        while heap:
            count, char = heappop(heap)
            if len(res) > 1 and res[-1] == res[-2] == char:
                if not heap:
                    break
                count2, char2 = heappop(heap)
                res += char2
                count2 += 1
                if count2:
                    heappush(heap, (count2, char2))
            else:
                res += char
                count += 1
            if count:
                heappush(heap, (count, char))
        return res

solution = Solution()
a = 1
b = 1
c = 7
assert solution.longestDiverseString(a, b, c) == 'ccaccbcc', "Should be 'ccaccbcc'"