class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        min_heap = []
        for num in nums:
            if len(min_heap) == k:
                if num >= min_heap[0]:
                    heapq.heappushpop(min_heap, num)
            else:
                heapq.heappush(min_heap, num)
        return min_heap[0]