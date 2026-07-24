class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = {}
        n = len(nums)

        def dfs(curr_idx, curr_sum):
            if ((curr_idx, curr_sum)) in dp:
                return dp[(curr_idx, curr_sum)]
            if curr_idx > n:
                return 0
            if curr_idx == n:
                if curr_sum == target:
                    return 1
                else:
                    return 0
            res = dfs(curr_idx + 1, curr_sum - nums[curr_idx]) + dfs(curr_idx + 1, curr_sum + nums[curr_idx])
            dp[(curr_idx, curr_sum)] = res
            return res
            

        return dfs(0, 0) # curr index, curr sum