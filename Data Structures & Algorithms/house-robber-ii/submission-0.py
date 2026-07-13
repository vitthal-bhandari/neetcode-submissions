class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)<3:
            return max(nums)
        def robHouse(numsArr):
            rob1, rob2=0, 0
            for num in numsArr:
                temp=max(rob1+num, rob2)
                rob1=rob2
                rob2=temp
            return rob2
        return max(robHouse(nums[1:]), robHouse(nums[:-1]))