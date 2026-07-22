class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS, res = len(grid), len(grid[0]), 0
        def dfs(i, j):
            if i not in range(ROWS) or j not in range(COLS) or grid[i][j] != 1:
                return 0
            grid[i][j] = 0
            return 1 + dfs(i+1, j) + dfs(i-1, j) + dfs(i, j+1) + dfs(i, j-1)
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 1:
                    res = max(res, dfs(i, j))
        return res