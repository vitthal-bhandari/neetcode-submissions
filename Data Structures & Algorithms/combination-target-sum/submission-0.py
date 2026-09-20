class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        nums.sort()
        subset = []
        def dfs(i, s):
            if s == target:
                res.append(subset.copy())
                return
            for j in range(i, len(nums)):
                if s + nums[j]>target:
                    return
                subset.append(nums[j])
                dfs(j, s+nums[j])
                subset.pop()
        dfs(0, 0)
        return res