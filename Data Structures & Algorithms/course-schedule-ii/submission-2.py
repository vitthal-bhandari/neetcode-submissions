class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        preMap = defaultdict(list)
        for a, b in prerequisites:
            preMap[b].append(a)
        visit = {}
        res = []
        def dfs(crs):
            if crs in visit:
                return visit[crs]
            visit[crs] = False
            for nei in preMap[crs]:
                if not dfs(nei):
                    return False
            visit[crs] = True
            preMap[crs] = []
            res.append(crs)
            return True
        for i in range(numCourses):
            if not dfs(i):
                return []
        return res[::-1]