class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return
        target = nums[0]
        for i in range(1, len(nums)):
            target ^= nums[i]
        return target


print Solution().singleNumber([1, 2, 2])
