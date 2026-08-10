class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = collections.defaultdict(list)
        for u, v, w in times:
            adj[u].append((v, w))
        minHeap =[(0, k)]
        visit = set()
        t = 0
        while minHeap:
            w, v = heapq.heappop(minHeap)
            if v in visit:
                continue
            visit.add(v)
            t = max(t, w)
            for nei, wei in adj[v]:
                if nei not in visit:
                    heapq.heappush(minHeap, (wei + w, nei))
        return t if len(visit) == n else -1