class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        q = deque()
        n = len(temperatures)
        res = [0] * n
        for i in range(n):
            if not len(q):
                q.append((temperatures[i], i))
                continue
            while q and temperatures[i] > q[0][0]:
                temp, idx = q.popleft()
                res[idx] = i - idx
            q.appendleft((temperatures[i], i))
        return res