class Solution:
    def climbStairs(self, n: int) -> int:
        sq5 = math.sqrt(5)
        a, b = (1+sq5)/2, (1-sq5)/2
        n += 1
        return round((a**n - b**n)/sq5)