class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        dp, dp1, dp2 = 0, 1, 0
        for i in range(n-1, -1, -1):
            if s[i] == '0':
                dp = 0
            elif i+1 < n and '10' <= s[i:i+2] <= '26':
                dp = dp1 + dp2
            else:
                dp = dp1
            dp1, dp2 = dp, dp1
        return dp1