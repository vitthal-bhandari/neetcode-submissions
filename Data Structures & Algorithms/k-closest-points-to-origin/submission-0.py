class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minH = []
        for x, y in points:
            dist = math.sqrt(x*x + y*y)
            if len(minH) < k:
                # simply push
                heapq.heappush_max(minH, (dist, x, y))
            else:
                # prioritize
                if dist < minH[0][0]:
                    heapq.heapreplace_max(minH, (dist, x, y))
        res = []
        while minH:
            _, x, y = heapq.heappop_max(minH)
            res.append([x, y])
        return res