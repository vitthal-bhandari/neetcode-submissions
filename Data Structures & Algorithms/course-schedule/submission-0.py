class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap = defaultdict(list)
        for a, b in prerequisites:
            preMap[a].append(b)
        visit = set()

        def dfs(course):
            if course in visit:
                return False
            if not preMap[course]:
                return True
            visit.add(course)
            for prereq in preMap[course]:
                if not dfs(prereq):
                    return False
            visit.remove(course)
            preMap[course] = []
            return True
        
        for course in range(numCourses):
            if not dfs(course):
                return False
        return True