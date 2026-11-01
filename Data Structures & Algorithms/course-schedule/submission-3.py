class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = defaultdict(list)
        for a, b in prerequisites:
            adj[a].append(b)
        visit = {}
        def dfs(node):
            if node in visit:
                return visit[node]
            visit[node] = True
            for nei in adj[node]:
                if dfs(nei):
                    return True
            visit[node] = False
        for i in range(numCourses):
            if dfs(i):
                return False
        return True
