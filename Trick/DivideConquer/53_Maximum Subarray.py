class Solution:
    def __init__(self):
        nums = []

    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        self.nums = nums
        return self.findMax(0, len(nums))

    def findMax(self, start, end):
        if (start == end - 1 or start == end):
            return self.nums[start]
        mid = int((start + end) / 2)
        leftMax = self.findMax(start, mid)
        rightMax = self.findMax(mid, end)
        midMax = self.findCross(start, end)
        return max(leftMax, rightMax, midMax)

# Max subarray cross the middle element
    def findCross(self, start, end):
        if start == end - 1 or start == end:
            return self.nums[start]
        mid = int((start + end) / 2)
        current = self.nums[mid]
        ret = current

        for i in range(mid + 1, end):
            current += self.nums[i]
            if current > ret:
                ret = current
        current = ret
        for i in range(mid - 1, start - 1, -1):
            current+=self.nums[i]
            if current > ret:
                ret = current
        return ret


print Solution().maxSubArray([1, 3, -1, 2, 0, -2, 2])
