class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        targetIdx = -1
        for i in range(len(nums) - 1, 0, -1):
            if nums[i] > nums[i - 1]:
                targetIdx = i - 1
                break
        if targetIdx == -1:
            nums.reverse()
            return
        for i in range(len(nums) - 1, 0, -1):
            if nums[i] > nums[targetIdx]:
                tep = nums[targetIdx]
                nums[targetIdx] = nums[i]
                nums[i] = tep
                break
        nums[targetIdx + 1:] = reversed(nums[targetIdx + 1:])


a = [3,2,1]
Solution().nextPermutation(a)
print a
