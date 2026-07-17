class TrieNode:

    def __init__(self):
        self.children = [None]*26
        self.endOfWord = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        node = self.root
        for c in word:
            index = ord(c) - ord('a')
            if node.children[index] == None:
                node.children[index] = TrieNode()
            node = node.children[index]
        node.endOfWord = True

    def search(self, word: str) -> bool:
        node = self.root
        return self.searchWildcard(word, node)
        
    def searchWildcard(self, word: str, node: TrieNode) -> bool:
        for i in range(len(word)):
            flag = False
            if word[i] == '.':
                for index in range(26):
                    if node.children[index] != None and self.searchWildcard(word[i+1:], node.children[index]):
                        flag = True
                        break
                return flag
            else:
                index = ord(word[i]) - ord('a')
                if node.children[index] == None:
                    return False
                node = node.children[index]
        return node.endOfWord
        
