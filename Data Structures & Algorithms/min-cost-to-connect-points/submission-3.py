class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        # Optimal Prim's Algorithm
        # T(n) = n**2, S(n) = n
        res, edges, node, n = 0, 0, 0, len(points)
        visit = [False]*n
        dist = [float("inf")]*n

        while edges < n-1:
            visit[node] = True
            nextNode = -1
            for i in range(n):
                if not visit[i]:
                    currDist = abs(points[node][0] - points[i][0]) + abs(points[node][1] - points[i][1])
                    if currDist < dist[i]:
                        dist[i] = currDist
                    if nextNode == -1 or dist[i] < dist[nextNode]:
                        nextNode = i
            res += dist[nextNode]
            edges += 1
            node = nextNode
        
        return res