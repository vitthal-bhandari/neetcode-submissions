class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        area = min(heights[l], heights[r]) * (r-l)
        while l < r:
            if heights[r] > heights[l]:
                l+=1
            else:
                r-=1
            area = max(area, min(heights[l], heights[r]) * (r-l))
        return area