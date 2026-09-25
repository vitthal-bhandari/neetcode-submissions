class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        indegree = [0]*numCourses
        preMap = defaultdict(list)
        for a, b in prerequisites:
            indegree[a] += 1
            preMap[b].append(a)
        q = deque()
        res = []
        for i in range(numCourses):
            if not indegree[i]:
                q.append(i)
        while q:
            crs = q.popleft()
            res.append(crs)
            for nei in preMap[crs]:
                indegree[nei] -= 1
                if not indegree[nei]:
                    q.append(nei)
        return res if len(res) == numCourses else []