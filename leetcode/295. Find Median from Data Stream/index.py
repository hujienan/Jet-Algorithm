from bisect import insort
from heapq import heappop, heappush


class MedianFinder1:

    def __init__(self):
        self.nums = []
        
    def addNum(self, num: int) -> None:
        insort(self.nums, num)
        
    def findMedian(self) -> float:
        length = len(self.nums)
        if length % 2:
            return self.nums[length // 2]
        return (self.nums[length // 2] + self.nums[(length // 2) - 1]) / 2

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()

class MedianFinder2:

    def __init__(self):
        self.small = []
        self.large = []

    def addNum(self, num: int) -> None:
        heappush(self.small, -1 * num)
        
        if self.small and self.large and -1 * self.small[0] > self.large[0]:
            val = -1 * heappop(self.small)
            heappush(self.large, val)
        
        if len(self.small)  - 2 == len(self.large):
            val = -1 * heappop(self.small)
            heappush(self.large, val)
        
        if len(self.small) == len(self.large) - 2:
            val = -1 * heappop(self.large)
            heappush(self.small, val)
        
    def findMedian(self) -> float:
        if (len(self.small) + len(self.large)) % 2 == 0:
            return (-1 * self.small[0] + self.large[0]) / 2      
        if len(self.small) > len(self.large):
            return -1 * self.small[0]
        return self.large[0]


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()