class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        lo, hi = 0, len(nums) - 1
        core = -1
        while lo <= hi:
            mid = (lo + hi) // 2
            if nums[mid] < target:
                lo = mid + 1
            elif nums[mid] > target:
                hi = mid - 1
            else:
                core = mid
                break
        left, right = core, core
        if core != -1:
            while left > 0 and nums[left - 1] == target:
                left -= 1
            while right + 1 < len(nums) and nums[right + 1] == target:
                right += 1
        return [left, right]


print Solution().searchRange([5, 7, 7, 8, 8, 10], 8)
