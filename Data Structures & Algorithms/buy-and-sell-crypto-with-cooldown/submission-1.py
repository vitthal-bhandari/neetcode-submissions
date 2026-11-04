class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp1_buy, dp1_sell, dp2_buy = 0, 0, 0
        for i in range(len(prices) - 1, -1, -1):
            # buy some stock
            buy = max(dp1_sell - prices[i], dp1_buy)
            # or sell some stock
            sell = max(dp2_buy + prices[i], dp1_sell)
            # now update variables before going back 1 day
            dp2_buy = dp1_buy
            dp1_buy, dp1_sell = buy, sell
        return dp1_buy