class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        dp = defaultdict(lambda: (0, 0))
        target = [sum(nums)]
        if target[0] % 2 == 1:
            return False
        else:
            target[0] //= 2
        def dfs(t, i):
            if (t, i) in dp:
                return dp[(t, i)]
            if t == target[0]:
                return True
            if t > target[0] or i >= len(nums):
                return False
            res = dfs(t + nums[i], i + 1) or dfs(t, i + 1)
            dp[(t, i)] = res
            return res
        
        return dfs(0, 0)