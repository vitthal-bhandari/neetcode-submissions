import random

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        def quickSelect(nums, k):
            left, mid, right = [], [], []
            pivot = random.choice(nums)
            for num in nums:
                if num > pivot: # bec quickselect is for k-th largest, we reverse order here
                    left.append(num)
                elif num < pivot:
                    right.append(num)
                else:
                    mid.append(num)
            if len(left) >= k:
                return quickSelect(left, k)
            elif len(left) + len(mid) < k:
                return quickSelect(right, k - len(left) - len(mid))
            else:
                return pivot
        return quickSelect(nums,k)