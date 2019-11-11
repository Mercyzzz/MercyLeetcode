class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        self.dfs(nums, [], res, len(nums))
        return res

    def dfs(self, nums, tep, res, length):
        if len(tep) == length:
            res.append(tep)
        for i in range(len(nums)):
            self.dfs(nums[:i] + nums[i + 1:], tep + [nums[i]], res, length)


print Solution().permute([1, 2, 3])
