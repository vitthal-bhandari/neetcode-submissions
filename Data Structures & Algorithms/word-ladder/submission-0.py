class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        dp = defaultdict(list)
        for word in wordList:
            n = len(word)
            for i in range(n):
                tmp = word[:i] + '*' + word[i+1:]
                dp[tmp].append(word)
        q = deque([beginWord])
        res = 1
        while q:
            for _ in range(len(q)):
                word = q.popleft()
                if word == endWord:
                    return res
                n = len(word)
                for i in range(n):
                    tmp = word[:i] + '*' + word[i+1:]
                    for wordNext in dp[tmp]:
                        if wordNext != word:
                            q.append(wordNext)
                    dp[tmp] = []
            res += 1
        return 0