class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adj = {c: set() for word in words for c in word }
        for i in range(len(words) - 1):
            j = i+1
            # compare words[i] and words[j]
            l1, l2 = len(words[i]), len(words[j])
            minLen = min(l1, l2)
            if l1 > l2 and words[i][:minLen] == words[j][:minLen]:
                return ""
            for k in range(minLen):
                if words[i][k] != words[j][k]:
                    adj[words[i][k]].add(words[j][k])
                    break
        visit = {}
        res = ''
        def dfs(c):
            nonlocal res
            if c in visit:
                return visit[c]
            visit[c] = True
            for nei in adj[c]:
                if dfs(nei):
                    return True
            visit[c] = False
            res += c

        for char in adj:
            if dfs(char):
                return ""
        return res[::-1]