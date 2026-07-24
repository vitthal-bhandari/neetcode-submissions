class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS, COLS = len(board), len(board[0])

        def dfs(i, j):
            if i not in range(ROWS) or j not in range(COLS) or board[i][j] != 'O':
                return
            board[i][j] = 'T'
            dfs(i+1, j)
            dfs(i-1, j)
            dfs(i, j+1)
            dfs(i, j-1)

        for i in range(ROWS):
            if board[i][0] == 'O':
                dfs(i, 0)
            if board[i][COLS-1] == 'O':
                dfs(i, COLS-1)
        for j in range(COLS):
            if board[0][j] == 'O':
                dfs(0, j)
            if board[ROWS-1][j] == 'O':
                dfs(ROWS-1, j)
        
        for i in range(ROWS):
            for j in range(COLS):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                elif board[i][j] == 'T':
                    board[i][j] = 'O'