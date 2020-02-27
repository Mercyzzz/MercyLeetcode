import heapq
import random


class Solution(object):
    def findKthLargest(self, nums, k):
        heapq.heapify(nums)
        for i in range(len(nums) - k):
            heapq.heappop(nums)
        return heapq.heappop(nums)

    def findKthLargestHeap(self, nums, k):
        for i in range(len(nums) / 2, -1, -1):
            self.heapify(nums, i, len(nums))
        for i in range(len(nums) - 1, k - 1, - 1):
            nums[i], nums[0] = nums[0], nums[i]
            self.heapify(nums, 0, i)
        return nums[0]

    def heapify(self, nums, start, end):
        root = start
        child = start * 2 + 1
        while child < end:
            right = child + 1
            if right < end and nums[right] < nums[child]:
                child = right
            if nums[child] < nums[root]:
                nums[root], nums[child] = nums[child], nums[root]
                root = child
                child = root * 2 + 1
            else:
                break

    def findKthLargest1(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        return self.qs(nums, 0, len(nums) - 1, k)

    def qs(self, nums, left, right, k):
        idx = (left + right) // 2
        nums[right], nums[idx] = nums[idx], nums[right]
        pivot = nums[right]
        pos = left
        for i in range(left, right):
            if nums[i] >= pivot:
                nums[i], nums[pos] = nums[pos], nums[i]
                pos += 1
        nums[pos], nums[right] = nums[right], nums[pos]
        if pos + 1 == k:
            return nums[pos]
        elif pos + 1 > k:
            return self.qs(nums, left, pos - 1, k)
        else:
            return self.qs(nums, pos + 1, right, k)

print Solution().findKthLargest1([3, 2, 1, 5, 6, 4], 6)

print Solution().heapify([])