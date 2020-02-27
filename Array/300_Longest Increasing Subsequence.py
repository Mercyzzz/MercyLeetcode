class Solution(object):
    def lengthOfLIS1(self, nums):
        dp = []
        for i in range(len(nums)):
            left, right = 0, len(dp)
            while left < right:
                mid = (left + right) / 2
                if dp[mid] < nums[i]:
                    left = mid + 1
                else:
                    right = mid
            if right >= len(dp):
                dp.append(nums[i])
            else:
                dp[right] = nums[i]
        return len(dp)
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dp = [1 for i in nums]
        for i in range(len(nums)):
            for j in range(0, i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)


print Solution().lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18, 9, 8])
