class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0
        dp = [0] * len(prices)

        minPrice = prices[0]
        for i in range(1, len(prices)):
            dp[i] = max(dp[i - 1], prices[i] - minPrice)
            if prices[i] < minPrice:
                minPrice = prices[i]
        return dp[-1]


print Solution().maxProfit([7, 1, 5, 3, 6, 4])
