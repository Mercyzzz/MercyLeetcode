class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length = len(nums)
        i = 0
        while i < length:
            while 0 < nums[i] < length + 1 and nums[nums[i] - 1] != nums[i]:
                nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]
            i += 1
        for i in range(length):
            if nums[i] - 1 != i:
                return i + 1
        return length + 1

print Solution().firstMissingPositive([-1, 5, 1, 4, 2])
