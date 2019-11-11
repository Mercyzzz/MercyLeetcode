class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dp = [i for i in nums]
        for i in range(1, len(nums)):
            dp[i] = max(dp[i], dp[i - 1] + nums[i])
        return max(dp)


print Solution().maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4])
