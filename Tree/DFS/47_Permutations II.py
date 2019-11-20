class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        res = []
        self.dfs(nums, [], res, len(nums))
        return res

    def dfs(self, nums, tep, res, length):
        if len(tep) == length:
            res.append(tep)
        for i in range(len(nums)):
            if i != 0 and nums[i] == nums[i - 1]:
                continue
            self.dfs(nums[:i] + nums[i + 1:], tep + [nums[i]], res, length)


print Solution().permuteUnique([3, 3, 0, 3])
