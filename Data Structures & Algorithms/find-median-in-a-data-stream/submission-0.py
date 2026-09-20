class MedianFinder:
    def __init__(self):
        self.small, self.large = [],[]

    def addNum(self, num: int) -> None:
        # by default add the element to the small heap, but since python only implements min heap but we want a max heap for the small heap we insert the -1 * val
        heapq.heappush(self.small, -1*num)

        #check if the elements in the small heap <= elements in the large heap
        if (self.small and self.large and -1*self.small[0] > self.large[0]):
            val = -1 * heapq.heappop(self.small)
            heapq.heappush(self.large, val)

        #check if the size of the heaps vary by more than one
        if len(self.small) > len(self.large) + 1:
            val = -1 * heapq.heappop(self.small)
            heapq.heappush(self.large, val)
        if len(self.large) > len(self.small) + 1:
            val = heapq.heappop(self.large)
            heapq.heappush(self.small, -1 * val)

    def findMedian(self) -> float:
        if len(self.small) > len(self.large):
            return -1 * self.small[0]
        if len(self.large) > len(self.small):
            return self.large[0]
        else:
            return (-1*self.small[0] + self.large[0]) / 2
            
        
        