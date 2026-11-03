class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        res = [nums[0]]
        for num in nums[1:]:
            l, r  = 0, len(res) - 1
            if r >= 0 and num > res[r]:
                res.append(num)
                continue
            while l < r:
                mid = (l+r) // 2
                if num > res[mid]:
                    l = mid + 1
                else:
                    r = mid
            res[l] = num
        return len(res)