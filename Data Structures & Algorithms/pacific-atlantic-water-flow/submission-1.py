class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        pac, atl = set(), set()
        res = []
        def dfs(r, c, visit, prevHeight):
            if r not in range(ROWS) or c not in range(COLS) or (r, c) in visit or heights[r][c] < prevHeight:
                return
            visit.add((r, c))
            dfs(r+1, c, visit, heights[r][c])
            dfs(r-1, c, visit, heights[r][c])
            dfs(r, c+1, visit, heights[r][c])
            dfs(r, c-1, visit, heights[r][c])
        for i in range(ROWS):
            dfs(i, 0, pac, -1)
            dfs(i, COLS-1, atl, -1)
        for i in range(COLS):
            dfs(0, i, pac, -1)
            dfs(ROWS-1, i, atl, -1)
        for (r, c) in pac:
            if (r, c) in atl:
                res.append([r, c])
        return res