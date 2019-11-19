class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ret = []
        self.dfs(nums, [], ret)
        return ret

    def dfs(self, nums, tep, ret):
        if not nums:
            ret.append(tep)
            return
        self.dfs(nums[1:], tep + [nums[0]], ret)
        self.dfs(nums[1:], tep, ret)


print Solution().subsets([1, 2, 3])
