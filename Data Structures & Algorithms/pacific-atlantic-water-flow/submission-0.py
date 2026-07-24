class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        dp = [[-1]*(ROWS) for _ in range(COLS)]
        pac, atl = set(), set()

        def dfs(r, c, visit, prevHeight):
            if ((r, c)) in visit or r < 0 or c < 0 or r == ROWS or c == COLS or heights[r][c] < prevHeight:
                return
            visit.add((r, c))
            dfs(r + 1, c, visit, heights[r][c])
            dfs(r, c+1, visit, heights[r][c])
            dfs(r - 1, c, visit, heights[r][c])
            dfs(r , c-1, visit, heights[r][c])
        
        # dp[i][j] = 0 -> can reach atlantic, 1 -> can reach pacific, 2 -> both
        for i in range(ROWS):
            dfs(i, 0, pac, heights[i][0])
            dfs(i, COLS-1, atl, heights[i][COLS-1])
        for j in range(COLS):
            dfs(0, j, pac, heights[0][j])
            dfs(ROWS-1, j, atl, heights[ROWS-1][j])
        
        res = []
        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) in pac and (r, c) in atl:
                    res.append([r, c])
        return res