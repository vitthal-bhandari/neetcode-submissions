class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False
        if len(s1) > len(s2):
            s1, s2 = s2, s1
        m, n = len(s1), len(s2)
        dp = [False] * (n + 1)
        dp[-1] = True
        for i in range(m, -1, -1):
            nextDp = [False] * (n + 1)
            if i == m:
                nextDp[n] = True
            for j in range(n, -1, -1):
                if i < m and s1[i] == s3[i+j] and dp[j]:
                    nextDp[j] = True
                if j < n and s2[j] == s3[i+j] and nextDp[j+1]:
                    nextDp[j] = True
            dp = nextDp
        return dp[0]