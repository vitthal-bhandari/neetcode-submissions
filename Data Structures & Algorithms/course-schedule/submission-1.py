class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegree = [0] * numCourses
        adj = defaultdict(list)
        for a, b in prerequisites:
            adj[b].append(a)
            # here directionally, we store all parent courses of a node
            indegree[a] += 1
        # if a node has a nonzero indegree, it means it has some
        # prerequisite(s) ! so don't get confused about the direction
        q = deque()
        finish = 0
        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)
        while q:
            course = q.popleft()
            finish += 1
            for nei in adj[course]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    q.append(nei)
        return finish == numCourses
