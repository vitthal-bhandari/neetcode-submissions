class TrieNode:

    def __init__(self):
        self.children = [None]*26
        self.idx = -1
        self.refs = 0

class Trie:

    def __init__(self):
        self.root = TrieNode()
    
    def addWord(self, word, i):
        node = self.root
        node.refs += 1
        for c in word:
            idx = ord(c) - ord('a')
            if node.children[idx] == None:
                node.children[idx] = TrieNode()
            node = node.children[idx]
            node.refs += 1
        node.idx = i
    
    def searchWord(self, word):
        node = self.root
        for c in word:
            idx = ord(c) - ord('a')
            if node.children[idx] == None:
                return False
            node = node.children[idx]
        return node.idx

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        node = Trie()
        res = []
        for i in range(len(words)):
            node.addWord(words[i], i)
        
        ROWS, COLS = len(board), len(board[0])
        
        def getIdx(w):
            return ord(w) - ord('a')

        def dfs(r, c, node):
            if r not in range(ROWS) or c not in range(COLS) or board[r][c] == '*' or not node.children[getIdx(board[r][c])]:
                return
            
            temp = board[r][c]
            board[r][c] = '*'
            prev = node
            node = node.children[getIdx(temp)]
            if node.idx != -1:
                res.append(words[node.idx])
                node.idx = -1
                node.refs -= 1
                if not node.refs:
                    prev.children[getIdx(temp)] = None
                    node = None
                    board[r][c] = temp
                    return
            
            dfs(r+1, c, node)
            dfs(r-1, c, node)
            dfs(r, c+1, node)
            dfs(r, c-1, node)

            board[r][c] = temp
        
        for r in range(ROWS):
            for c in range(COLS):
                dfs(r, c, node.root)
        
        return res