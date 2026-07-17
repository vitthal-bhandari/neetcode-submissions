class TrieNode:

    def __init__(self):
        self.children = [None]*26
        self.endOfWord = False

class PrefixTree:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root
        for c in word:
            if node.children[ord(c)-ord('a')] == None:
                node.children[ord(c)-ord('a')] = TrieNode()
            node = node.children[ord(c)-ord('a')]
        node.endOfWord = True


    def search(self, word: str) -> bool:
        node = self.root
        for c in word:
            if node.children[ord(c)-ord('a')] == None:
                return False
            node = node.children[ord(c)-ord('a')]
        return node.endOfWord
        

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for c in prefix:
            if node.children[ord(c)-ord('a')] == None:
                return False
            node = node.children[ord(c)-ord('a')]
        return True