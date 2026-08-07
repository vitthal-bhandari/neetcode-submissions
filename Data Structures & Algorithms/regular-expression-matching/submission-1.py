class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m, n = len(s), len(p)
        dp = [[False]* (n+1) for _ in range(m+1)]
        dp[m][n] = True
        
        for i in range(m, -1, -1):
            newDp = [False]* (n+1)
            newDp[n] = ( i ==m )

            for j in range(n-1, -1, -1):
                match = False
                if i < m and (s[i] == p[j] or p[j] == '.'):
                        match = True
                if j+1 < n and p[j+1] == '*':
                    newDp[j] = newDp[j+2] or (match and dp[j])
                elif match:
                    newDp[j] = dp[j+1]
            
            dp = newDp
        return dp[0]