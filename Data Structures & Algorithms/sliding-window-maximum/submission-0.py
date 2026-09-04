class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        if k >= len(nums):
            return [max(nums)]*(len(nums)-k+1)
        q = deque()
        for i in range(k):
            while q and nums[i] > nums[q[-1]]:
                q.pop()
            q.append(i)
        res = []
        res.append(nums[q[0]])
        for i in range(k, len(nums)):
            if q[0] == i-k:
                q.popleft()
            while q and nums[i] >= nums[q[-1]]:
                q.pop()
            q.append(i)
            res.append(nums[q[0]])
        return res