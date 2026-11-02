class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        dp = defaultdict(list)
        if endWord not in wordList:
            return 0
        for word in wordList:
            for i in range(len(word)):
                tmp = word[:i] + '*' + word[i+1:]
                dp[tmp].append(word)
        q = deque([beginWord])
        visit = set([beginWord])
        res = 1
        while q:
            for _ in range(len(q)):
                w = q.popleft()
                if w == endWord:
                    return res
                for i in range(len(w)):
                    tmp = w[:i] + '*' + w[i+1:]
                    for nei in dp[tmp]:
                        if nei not in visit:
                            visit.add(nei)
                            q.append(nei)
            res += 1
        return 0