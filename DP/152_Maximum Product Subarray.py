class Solution(object):
    def maxProduct(self, nums):
        dpPos = [i for i in nums]
        dpNeg = [i for i in nums]
        for i in range(len(nums) -1):
            dpPos[i] = max(dpPos[i - 1] * nums[i], dpPos[i], dpNeg[i - 1] * nums[i])
            dpNeg[i] = min(dpPos[i - 1] * nums[i], dpNeg[i], dpNeg[i - 1] * nums[i])
        return max(dpPos)

    def maxProduct1(self, nums):
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


print Solution().maxProduct([-2, 3, -4])
