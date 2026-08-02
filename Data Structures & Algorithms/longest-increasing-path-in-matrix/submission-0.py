class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        res = 0
        ROWS, COLS = len(matrix), len(matrix[0])
        dp = {}
        dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        
        def dfs(i, j):
            if (i, j) in dp:
                return dp[(i, j)]
            best = 1
            for r, c in dirs:
                dr, dc = i+r, j+c
                if dr in range(ROWS) and dc in range(COLS) and matrix[dr][dc] > matrix[i][j]:
                    best = max(best, 1 + dfs(dr, dc))
            dp[(i, j)] = best
            return best
        
        for i in range(ROWS):
            for j in range(COLS):
                res = max(res, dfs(i, j))
        
        return res