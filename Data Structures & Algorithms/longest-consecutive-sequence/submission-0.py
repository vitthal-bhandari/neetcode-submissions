class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        bucket = set(nums)
        res = 0
        for num in bucket:
            if num-1 not in bucket:
                l = 0
                while num + l in bucket:
                    l += 1
                res = max(l, res)
        return res