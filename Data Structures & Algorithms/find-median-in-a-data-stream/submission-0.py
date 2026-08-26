class MedianFinder:

    def __init__(self):
        self.minHeap, self.maxHeap = [], []

    def addNum(self, num: int) -> None:
        if self.minHeap and num > self.minHeap[0]:
            heapq.heappush(self.minHeap, num)
        else:
            heapq.heappush_max(self.maxHeap, num)
        if len(self.minHeap) > len(self.maxHeap) + 1:
            heapq.heappush_max(self.maxHeap, heapq.heappop(self.minHeap))
        if len(self.maxHeap) > len(self.minHeap) + 1:
            heapq.heappush(self.minHeap, heapq.heappop_max(self.maxHeap))
        

    def findMedian(self) -> float:
        if len(self.maxHeap) == len(self.minHeap):
            return (self.maxHeap[0] + self.minHeap[0]) / 2
        else:
            return self.maxHeap[0] if len(self.maxHeap) > len(self.minHeap) else self.minHeap[0]
        
        