class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heapq.heapify_max(stones)
        maxH = stones
        while maxH:
            heavy1 = heapq.heappop_max(maxH)
            if not maxH:
                return heavy1
            else:
                heavy2 = heapq.heappop_max(maxH)
                if heavy1 > heavy2:
                    heapq.heappush_max(maxH, heavy1 - heavy2)
        return maxH[0] if maxH else 0