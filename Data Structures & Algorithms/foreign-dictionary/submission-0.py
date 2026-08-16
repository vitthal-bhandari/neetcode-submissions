class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adj = {c: set() for word in words for c in word}
        for i in range(len(words)-1):
            j = i + 1
            minLen = min(len(words[i]), len(words[j]))
            if len(words[i]) > len(words[j]) and words[i][:minLen] == words[j][:minLen]:
                return ""
            for k in range(minLen):
                if words[i][k] == words[j][k]:
                    continue
                adj[words[i][k]].add(words[j][k])
                break
        
        visit = {}
        res = []
        def dfs(node):
            if node in visit:
                return visit[node]
            visit[node] = True
            for nei in adj[node]:
                if dfs(nei):
                    return True
            visit[node] = False
            res.append(node)
        for char in adj:
            if dfs(char):
                return ""
        res.reverse()
        return "".join(res)