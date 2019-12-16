class Solution(object):
    def jump(self, nums):
        n = len(nums)
        l = r = step = 0
        while r < n - 1:
            nr = r
            for i in range(l, r + 1):
                nr = max(nr, i + nums[i])
            step += 1
            l = r + 1
            r = nr
        return step

    def jump1(self,  nums):
        ret = last = cur = 0
        for i in range(len(nums)):
            if i > last:
                last = cur
                ret += 1
            cur = max(cur, i + nums[i])
        return ret


    def jumpDp(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dp = [float('inf') for i in nums]
        dp[-1] = 0
        for i in range(len(nums) - 2, -1, -1):
            right = min(len(nums), i + nums[i] + 1)
            for j in range(i + 1, right):
                dp[i] = min(dp[i], dp[j] + 1)
        return dp[0]


print Solution().jump([3, 4, 1, 1, 0, 1, 2])
