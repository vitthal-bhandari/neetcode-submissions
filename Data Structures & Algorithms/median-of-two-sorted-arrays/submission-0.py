class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        a, b = len(nums1), len(nums2)
        if a > b:
            nums1, nums2 = nums2, nums1
            a, b = b, a
        total = a + b
        half = total // 2

        l, r = 0, a - 1
        while True:
            i = (l + r) // 2
            j = half - i - 2
            Aleft = nums1[i] if i >= 0 else float("-inf")
            Aright = nums1[i+1] if i+1 < a else float("inf")
            Bleft = nums2[j] if j >= 0 else float("-inf")
            Bright = nums2[j+1] if j+1 < b else float("inf")

            if Aleft <= Bright and Bleft <= Aright:
                return min(Aright, Bright) if total % 2 == 1 else (max(Aleft, Bleft) + min(Aright, Bright)) / 2
            elif Aleft > Bright:
                r = i - 1
            else:
                l = i + 1
        return -1