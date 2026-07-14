class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        dp = {}
        dp[n] = 1
        def dfs(i):
            if i in dp:
                return dp[i]
            if i > n:
                return 0
            if s[i] == '0':
                return 0
            if i+1 < n and '10' <= s[i:i+2] <= '26':
                res = dfs(i+1) + dfs(i+2)
            else:
                res = dfs(i+1)
            dp[i] = res
            return res
        return dfs(0)