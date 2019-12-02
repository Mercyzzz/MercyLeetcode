class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        return self.qs(nums, 0, len(nums) - 1, k)

    def qs(self, nums, left, right, k):
        pivot = nums[right]
        pos = left
        for i in range(left, right):
            if nums[i] >= pivot:
                nums[i], nums[pos] = nums[pos], nums[i]
                pos += 1
        nums[pos], nums[right] = nums[right], nums[pos]
        if pos + 1 == k:
            return nums[pos]
        if pos + 1 > k:
            return self.qs(nums, left, pos - 1, k)
        if pos + 1 < k:
            return self.qs(nums, pos + 1, right, k)


print Solution().findKthLargest([3, 2, 1, 5, 6, 4], 1)
