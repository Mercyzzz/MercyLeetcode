class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        dp = [i for i in nums]
        if len(nums) > 1:
            dp[1] = max(dp[0], dp[1])
        for i in range(2, len(nums)):
            dp[i] = max(dp[i - 1], dp[i] + dp[i - 2])
        return max(dp)


print Solution().rob([2, 1, 1, 2])
