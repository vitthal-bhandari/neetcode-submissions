class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.minH, self.k = nums, k
        heapq.heapify(self.minH)
        while len(self.minH) > self.k:
            heapq.heappop(self.minH)
        

    def add(self, val: int) -> int:
        heapq.heappush(self.minH, val)
        if len(self.minH) > self.k:
            heapq.heappop(self.minH)
        return self.minH[0] if self.minH else -1
