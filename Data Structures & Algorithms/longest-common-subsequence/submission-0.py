class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m, n = len(text1), len(text2)
        if m < n:
            text1, text2 = text2, text1
            m, n = n, m
        prev = [0] * (n+1)
        for i in range(1, m+1):
            curr = [0] * (n+1)
            for j in range(1, n+1):
                curr[j] = 1 + prev[j-1] if text1[i-1] == text2[j-1] else max(prev[j], curr[j-1])
            prev = curr
        return prev[n]