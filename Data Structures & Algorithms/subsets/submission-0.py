class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        def addEle(i, comb):
            if i == len(nums):
                res.append(comb)
                return
            addEle(i+1, comb)
            addEle(i+1, comb + [nums[i]])
        addEle(0, [])
        return res