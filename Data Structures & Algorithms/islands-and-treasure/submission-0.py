class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS, COLS, INF = len(grid), len(grid[0]), 2**31 -1
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        q = deque()
        visit = set()
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 0:
                    q.append((i, j))
                    visit.add((i, j))
        dist = 1
        while q:
            for _ in range(len(q)):
                r, c = q.popleft()
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if nr not in range(ROWS) or nc not in range(COLS) or (nr, nc) in visit or grid[nr][nc] == -1:
                        continue
                    grid[nr][nc] = dist
                    q.append((nr, nc))
                    visit.add((nr, nc))
            dist += 1