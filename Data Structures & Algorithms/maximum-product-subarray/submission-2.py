class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res, prevMin, prevMax = nums[0], 1, 1
        for num in nums:
            temp = prevMin * num
            prevMin = min(prevMin * num, prevMax * num, num)
            prevMax =  max(temp, prevMax * num, num)
            res = max(res, prevMax)
        return res