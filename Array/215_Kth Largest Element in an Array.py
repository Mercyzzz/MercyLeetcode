import heapq
class Solution(object):
    def findKthLargest(self, nums, k):
        heapq.heapify(nums)
        for i in range(len(nums) - k):
            heapq.heappop(nums)
        print nums
        return [x for x in reversed([heapq.heappop(nums) for i in range(k)])]


    def findKthLargest1(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        return self.qs(nums, 0, len(nums) - 1, k)

    def qs(self, nums, left, right, k):
        if left >= right:
            return
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

#print Solution().qsS([3, 2, 1, 5, 6, 4])
print Solution().findKthLargest([3, 2, 1, 5, 6, 4], 5)
