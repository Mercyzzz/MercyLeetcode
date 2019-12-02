class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dpPos = [i for i in nums]
        dpNeg = [i for i in nums]
        for i in range(1, len(nums)):
            dpNeg[i] = min(nums[i], dpNeg[i - 1] * nums[i], dpPos[i - 1] * nums[i])
            dpPos[i] = max(nums[i], dpNeg[i - 1] * nums[i], dpPos[i - 1] * nums[i])
        return max(dpPos)


print Solution().maxProduct([-1, -2, -9, -6])
