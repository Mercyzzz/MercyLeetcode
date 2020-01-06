class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        pt = 0
        for i in range(len(nums)):
            while pt < len(nums) and nums[pt] != 0:
                pt += 1
            if pt >= len(nums):
                break
            if nums[i] != 0 and i > pt:
                nums[i], nums[pt] = nums[pt], nums[i]
