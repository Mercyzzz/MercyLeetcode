class Solution(object):
    def twoSum(self, nums, target, item):
        left, right = 0, len(nums) - 1
        minMinus = float('inf')
        minSum = float('inf')
        while left < right:
            sum = nums[left] + nums[right] + item
            if sum <= target:
                left += 1
            elif sum > target:
                right -= 1
            if abs(sum - target) < minMinus:
                minSum = sum
            minMinus = min(abs(sum - target), minMinus)
        return minSum

    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        minMinus = float('inf')
        minSum = float('inf')
        for i in range(len(nums) - 2):
            if (i == 0 or nums[i] > nums[i - 1]):
                tepMinSum = self.twoSum(nums[i + 1:], target, nums[i])
                if abs(tepMinSum - target) < minMinus:
                    minMinus = abs(tepMinSum - target)
                    minSum = tepMinSum
        return minSum


print Solution().threeSumClosest([0, 1, 2], 3)
