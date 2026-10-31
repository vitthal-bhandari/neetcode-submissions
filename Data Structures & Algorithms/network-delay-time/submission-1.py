class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = defaultdict(list)
        for u, v, w in times:
            adj[u].append((v, w))
        minH = [(0, k)]
        time = 0
        visit = set()
        while minH:
            weight, node = heapq.heappop(minH)
            if node in visit:
                continue
            visit.add(node)
            time = max(time, weight)
            for nei, wei in adj[node]:
                if nei not in visit:
                    heapq.heappush(minH, (weight + wei, nei))
        return time if len(visit) == n else -1