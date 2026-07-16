class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res, prev_min, prev_max = nums[0], nums[0], nums[0]
        for num in nums[1:]:
            if num <= 0:
                if prev_min <= 0:
                    if prev_max <= 0:
                        prev_max = prev_min*num
                        prev_min = num
                    else:
                        prev_max, prev_min = prev_min*num, prev_max*num
                else:
                    prev_min = prev_max*num
                    prev_max = num
            else:
                if prev_min <= 0:
                    if prev_max <= 0:
                        prev_max = num
                        prev_min = prev_min*num
                    else:
                        prev_max *= num
                        prev_min *= num
                else:
                    prev_max *= num
                    prev_min *= num
            res = max(res, prev_max)
        return res