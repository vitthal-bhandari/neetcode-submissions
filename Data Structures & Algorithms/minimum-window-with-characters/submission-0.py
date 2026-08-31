class Solution:
    def minWindow(self, s: str, t: str) -> str:
        m, n = len(s), len(t)
        if m < n:
            return ""
        l, res, reslen = 0, "", float("inf")
        window_s, window_t = {}, {}
        for i in range(n):
            window_t[t[i]] = window_t.get(t[i],0) + 1
            window_s[s[i]] = window_s.get(s[i],0) + 1
        need, have = len(window_t), 0
        for k, v in window_t.items():
            if k in window_s and v <= window_s[k]:
                have += 1
        if have == need:
            reslen = n
            res = s[:n]
        for r in range(n, m):
            print(s[r])
            if have == need:
                if r - l + 1 < reslen:
                    reslen = r - l + 1
                    res = s[l: r+1]
            window_s[s[r]] = window_s.get(s[r],0) + 1
            if s[r] in window_t and window_s[s[r]] == window_t[s[r]]:
                have += 1
            while have == need:
                if r - l + 1 < reslen:
                    reslen = r - l + 1
                    res = s[l: r+1]
                window_s[s[l]] = window_s.get(s[l],0) - 1
                if s[l] in window_t and window_s[s[l]] < window_t[s[l]]:
                    have -= 1
                l += 1
        return s if m == n and have == need else res