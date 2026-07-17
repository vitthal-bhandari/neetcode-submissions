class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        res = [nums[0]]
        for num in nums[1:]:
            l, r = 0, len(res) - 1
            if r >= 0 and num > res[r]:
                res.append(num)
                continue
            while l < r:
                m = (l + r) // 2
                if num > res[m]:
                    l = m + 1
                else:
                    r = m
            res[l] = num
        return len(res)