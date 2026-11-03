class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        dp = [False] * (n) + [True]
        for i in range(n-1, -1, -1):
            for word in wordDict:
                l = len(word)
                if i + l <= n and s[i: i+l] == word:
                    dp[i] = dp[i+l]
                if dp[i]:
                    break
        return dp[0]