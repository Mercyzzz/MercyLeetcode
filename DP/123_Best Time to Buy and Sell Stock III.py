class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) < 2:
            return 0
        preProfit = [0] * len(prices)
        postProfit = [0] * len(prices)

        curMin = prices[0]
        for i in range(1, len(prices)):
            curMin = min(prices[i], curMin)
            preProfit[i] = max(preProfit[i - 1], prices[i] - curMin)

        curMax = prices[-1]
        for i in range(len(prices) - 2, -1, -1):
            curMax = max(prices[i], curMax)
            postProfit[i] = max(postProfit[i + 1], curMax - prices[i])

        maxProfit = 0
        for i in range(len(preProfit)):
            maxProfit = max(maxProfit, preProfit[i] + postProfit[i])
        return maxProfit

print Solution().maxProfit([1,2])