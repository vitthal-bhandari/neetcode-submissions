class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res, prev_min, prev_max = nums[0], 1, 1
        for num in nums:
            temp = prev_max*num
            prev_max = max(prev_max*num, prev_min*num, num)
            prev_min = min(prev_min*num, temp, num)
            res = max(res, prev_max)
        return res