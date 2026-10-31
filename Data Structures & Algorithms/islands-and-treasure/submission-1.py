class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS, COLS, INF = len(grid), len(grid[0]), 2**31-1
        q = deque()
        visit = set()
        dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 0:
                    q.append((i, j))
                    visit.add((i, j))
        dist = 1
        while q:
            for _ in range(len(q)):
                r, c = q.popleft()
                for x, y in dirs:
                    dr, dc = r+x, c+y
                    if dr not in range(ROWS) or dc not in range(COLS) or (dr, dc) in visit or grid[dr][dc] == -1:
                        continue
                    visit.add((dr, dc))
                    grid[dr][dc] = dist
                    q.append((dr, dc))
            dist += 1