class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        minHeap = [(grid[0][0], 0, 0)]
        visit = set()
        while minHeap:
            weight, r, c = heapq.heappop(minHeap)
            if r == ROWS-1 and c == COLS-1:
                return weight
            if (r, c) in visit:
                continue
            visit.add((r, c))
            for i, j in dirs:
                dr, dc = r+i, c+j
                if dr in range(ROWS) and dc in range(COLS) and (dr, dc) not in visit:
                    heapq.heappush(minHeap, (max(weight, grid[dr][dc]), dr, dc))
        return -1