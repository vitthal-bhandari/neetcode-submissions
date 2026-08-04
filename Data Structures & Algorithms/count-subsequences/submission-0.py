class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        m, n = len(s), len(t)
        if n > m:
            return 0
        dp = [0]*(n+1)
        dp[n] = 1
        for i in range(m-1, -1, -1):
            nextDp = [0]*(n+1)
            nextDp[n] = 1
            for j in range(n-1, -1, -1):
                nextDp[j] = dp[j]
                if s[i] == t[j]:
                    nextDp[j] += dp[j+1]
            dp = nextDp
        return dp[0]