class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # Kahn's algo solution
        indegree = [0] * numCourses
        adj = defaultdict(list)
        for a, b in prerequisites:
            adj[b].append(a)
            indegree[a] += 1
        q = deque()
        res = [] # replacing finish == numCourses condition with len(res) == numCourses
        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)
        while q:
            course = q.popleft()
            res.append(course)
            for nei in adj[course]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    q.append(nei)
        return res if len(res) == numCourses else []