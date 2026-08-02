class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        LIS = 0
        ROWS, COLS = len(matrix), len(matrix[0])
        dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        indegree = [[0]*COLS for _ in range(ROWS)]
        q = deque()
        for i in range(ROWS):
            for j in range(COLS):
                for a, b in dirs:
                    if i+a in range(ROWS) and j+b in range(COLS) and matrix[i+a][j+b] < matrix[i][j]:
                        indegree[i][j] += 1
                if indegree[i][j] == 0:
                    q.append((i, j))
        while q:
            for _ in range(len(q)):
                i, j = q.popleft()
                for a, b in dirs:
                    if i+a in range(ROWS) and j+b in range(COLS) and matrix[i+a][j+b] > matrix[i][j]:
                        indegree[i+a][j+b] -= 1
                        if indegree[i+a][j+b] == 0:
                            q.append((i+a, j+b))
            LIS += 1
        return LIS