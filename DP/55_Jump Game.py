class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) < 2:
            return True
        dp = [0 for i in nums]
        for i in range(len(nums) - 1):
            dp[i] = max(dp[i - 1] - 1, nums[i])
            if dp[i] == 0:
                return False
        return True


print Solution().canJump([0, 0])
