class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        # Regular Prim's Algorithm
        # T(n) = , S(n) =
        adj = defaultdict(list)
        for i in range(len(points)):
            for j in range(i+1, len(points)):
                dist = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                adj[i].append((dist, j))
                adj[j].append((dist, i))
        res = 0
        visit = set()
        minH = [(0, 0)] # (initial cost, initial idx)
        while len(visit) < len(points):
            cost, idx = heapq.heappop(minH)
            if idx in visit:
                continue
            visit.add(idx)
            res += cost
            for wei, nei in adj[idx]:
                if nei not in visit:
                    heapq.heappush(minH, (wei, nei))
        return res