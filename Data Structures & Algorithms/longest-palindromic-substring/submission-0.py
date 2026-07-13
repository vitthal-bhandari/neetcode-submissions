class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        res = ''
        for i in range(n):

            # check even length palindrome
            l, r, pl = i, i+1, 0
            while 0<=l<n and 0<=r<n and s[l] == s[r]:
                l-=1
                r+=1
                pl+=2
            if pl > len(res):
                res = s[l+1: r]

            # check odd length palindrome
            l, r, pl = i-1, i+1, 1
            while 0<=l<n and 0<=r<n and s[l] == s[r]:
                l-=1
                r+=1
                pl+=2
            if pl > len(res):
                res = s[l+1: r]
        return res