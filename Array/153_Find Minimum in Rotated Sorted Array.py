class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left, right = 0, len(nums) - 1
        if len(nums) == 1 or nums[left] < nums[right]:
            return nums[0]
        while left <= right:
            mid = (left + right) // 2
            if nums[left] < nums[mid]:
                left = mid + 1
            elif nums[left] > nums[mid]:
                right = mid - 1
            else:
                left += 1
            if left > len(nums) - 1:
                return nums[left - 1]
            if nums[left] < nums[left - 1]:
                return nums[left]
        return -1


print Solution().findMin([2, 2, 2, 2, 2])
