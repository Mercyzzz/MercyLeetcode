class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 0
        while i < len(nums):
            if nums[i] - 1 == i:
                i += 1
                continue
            if nums[nums[i] - 1] == nums[i]:
                return nums[i]
            nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]

