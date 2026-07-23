class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)
        coins.sort()
        dp = [0] * (amount+1)
        dp[0] = 1
        for i in range(n-1, -1, -1):
            nextDP = [0] * (amount + 1)
            nextDP[0] = 1
            for a in range(1, amount + 1):
                if a >= coins[i]:
                    nextDP[a] = dp[a]
                    nextDP[a] += nextDP[a-coins[i]]
            dp = nextDP
        return dp[amount]