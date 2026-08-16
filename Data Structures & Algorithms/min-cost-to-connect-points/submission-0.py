class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        # prims algorithm
        adj = defaultdict(list)
        for i in range(len(points)):
            for j in range(len(points)):
                if i != j:
                    adj[i].append((j, abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])))
        minHeap = [(0, 0)]
        visit = set()
        cost = 0
        while len(visit) != len(points):
            weight, idx = heapq.heappop(minHeap)
            if idx in visit:
                continue
            cost += weight
            visit.add(idx)
            for nei, wei in adj[idx]:
                if nei not in visit:
                    heapq.heappush(minHeap, (wei, nei))
        return cost