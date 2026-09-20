class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])
        def dfs(i, j, idx):
            if idx == len(word):
                return True
            if i not in range(ROWS) or j not in range(COLS) or board[i][j] != word[idx] or board[i][j] == '-1':
                return False
            temp = board[i][j]
            board[i][j] = '-1'
            res = dfs(i+1, j, idx+1) or dfs(i-1, j, idx+1) or dfs(i, j+1, idx+1) or dfs(i, j-1, idx+1)
            board[i][j] = temp
            return res
        
        for i in range(ROWS):
            for j in range(COLS):
                if dfs(i, j, 0):
                    return True
        return False