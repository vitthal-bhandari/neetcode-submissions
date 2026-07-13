class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0
        n = len(s)
        for i in range(n):

            # count odd length palindromes
            l, r = i, i
            while 0 <= l < n and 0 <= r < n and s[l] == s[r]:
                res += 1
                l -= 1
                r += 1
            
            # count even length palindromes
            l, r = i, i+1
            while 0 <= l < n and 0 <= r < n and s[l] == s[r]:
                res += 1
                l -= 1
                r += 1
        return res