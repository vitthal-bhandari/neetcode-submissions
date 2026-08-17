class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        a, b = intervals[0][0], intervals[0][1]
        res = []
        for start, end in intervals[1:]:
            if start > b:
                res.append([a, b])
                a, b = start, end
                continue
            b = max(b, end)
        res.append([a, b])
        return res