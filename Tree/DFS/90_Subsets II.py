class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ret = []
        nums.sort()
        self.dfs(nums, [], ret, 0, True)
        return ret

    def dfs(self, nums, tep, ret, idx, pre):
        if idx == len(nums):
            ret.append(tep)
            return
        if not(not pre and nums > 1 and nums[idx] == nums[idx - 1]):
            self.dfs(nums, tep + [nums[idx]], ret, idx + 1, True)
        self.dfs(nums, tep, ret, idx + 1, False)


print Solution().subsetsWithDup([1, 2, 2])
