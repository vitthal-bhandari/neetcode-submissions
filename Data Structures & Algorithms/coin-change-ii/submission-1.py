class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)
        coins.sort()
        # dp[a] = number of ways of making amount a from idx i onwards
        dp = [0] * (amount+1)
        # 1 way of making amount 0 from index 0 onwards - choose no coins
        dp[0] = 1
        for i in range(n-1, -1, -1):
            newDp = [0] * (amount+1)
            newDp[0] = 1
            for a in range(1, amount+1):
                if a >= coins[i]:
                    # skip the current coin
                    newDp[a] = dp[a]
                    # or pick this coin and decrement target amount
                    newDp[a] += newDp[a-coins[i]]
            dp = newDp
        # return ways of making amount from idx 0 onwards
        return dp[amount]