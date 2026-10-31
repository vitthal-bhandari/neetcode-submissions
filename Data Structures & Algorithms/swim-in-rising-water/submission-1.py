class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        minH = [(grid[0][0], 0, 0)] # cost, row, col;
        visit = set()
        dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        while minH:
            cost, r, c = heapq.heappop(minH)
            if r == ROWS-1 and c == COLS-1:
                return cost
            if (r, c) in visit:
                continue
            visit.add((r, c))
            for dr, dc in dirs:
                x, y = r+dr, c+dc
                if x in range(ROWS) and y in range(COLS) and grid[x][y] not in visit:
                    heapq.heappush(minH, (max(cost, grid[x][y]), x, y))
        return -1