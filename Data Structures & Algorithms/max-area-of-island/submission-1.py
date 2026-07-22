class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS, res = len(grid), len(grid[0]), 0
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        def bfs(i, j):
            q = deque()
            grid[i][j] = 0
            q.append((i, j))
            area = 1

            while q:
                r, c = q.popleft()
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if nr not in range(ROWS) or nc not in range(COLS) or grid[nr][nc] != 1:
                        continue
                    q.append((nr, nc))
                    grid[nr][nc] = 0
                    area += 1
            return area
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 1:
                    res = max(res, bfs(i, j))
        return res