class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if not nums:
            return []
        if len(nums) == 1:
            return[0]
        lTr = [i for i in nums]
        rTl = [i for i in nums]
        for i in range(1, len(nums)):
            lTr[i] = lTr[i - 1] * lTr[i]
        for i in range(len(nums) - 2, -1, -1):
            rTl[i] = rTl[i + 1] * rTl[i]
        ret = [rTl[1]]
        for i in range(1, len(nums) - 1):
            ret.append(lTr[i - 1] * rTl[i + 1])
        ret.append(lTr[-2])
        return ret

print Solution().productExceptSelf([1, 2, 3, 4])