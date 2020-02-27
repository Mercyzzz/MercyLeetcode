class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        left, right = 0, 0
        sum = 0
        ret = len(nums) + 1
        while right < len(nums):
            while sum < s and right < len(nums):
                sum += nums[right]
                right += 1
            while sum >= s:
                ret = min(ret, right - left)
                sum -= nums[left]
                left += 1
        return 0 if ret == len(nums) + 1 else ret


print Solution().minSubArrayLen(11, [1,2,3,4,5])
