class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordset = set(wordDict)
        n = len(s)
        dp = [False] * (n+1)
        dp[-1] = True

        for i in range(n-1, -1, -1):
            for j in range(i+1, n+1):
                if s[i:j] in wordset and dp[j] == True:
                    dp[i] = True
        
        return dp[0]