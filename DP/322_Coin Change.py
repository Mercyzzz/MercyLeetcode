class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0
        for i in range(1, len(dp)):
            for j in coins:
                if i - j >= 0:
                    dp[i] = min(dp[i - j] + 1, dp[i])
        return -1 if dp[-1] == float('inf') else dp[-1]


print Solution().coinChange([1, 2, 5], 11)
