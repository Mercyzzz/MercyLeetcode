class Solution(object):
    # dp
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dp = [i for i in nums]
        for i in range(1, len(nums)):
            dp[i] = max(dp[i], dp[i - 1] + nums[i])
        return max(dp)
    # greedy
    def maxSubArr(self, nums):
        res = nums[0]
        tep = nums[0]
        for i in range(1, len(nums)):
            tep = max(nums[i], nums[i] + tep)
            res = max(tep, res)
        return res
print Solution().maxSubArr([-2, 1, -3, 4, -1, 2, 1, -5, 4])
