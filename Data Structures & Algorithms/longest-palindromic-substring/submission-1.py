class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        res, maxlen = '', 0
        for i in range(n):

            # check even length palindrome
            l, r = i, i+1
            while 0<=l<n and 0<=r<n and s[l] == s[r]:
                l-=1
                r+=1
            if r - l - 1 > maxlen:
                res = s[l+1: r]
                maxlen = r - l - 1

            # check odd length palindrome
            l, r = i, i
            while 0<=l<n and 0<=r<n and s[l] == s[r]:
                l-=1
                r+=1
            if r - l - 1 > maxlen:
                res = s[l+1: r]
                maxlen = r - l - 1
        return res