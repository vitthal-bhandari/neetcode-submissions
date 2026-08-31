class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for i in range(len(nums)):
            if nums[i] > 0:
                break
            if i > 0 and nums[i] == nums[i-1]:
                continue
            target = -1*nums[i]
            j, k = i+1, len(nums) - 1
            while j < k:
                if nums[j] + nums[k] > target:
                    k -=1
                elif nums[j] + nums[k] < target:
                    j += 1
                else:
                    res.append([nums[i], nums[j], nums[k]])
                    while j < k and nums[j] == nums[j+1]:
                        j += 1
                    j += 1
        return res