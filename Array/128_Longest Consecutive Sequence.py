class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        numSet = set(nums)
        ret = 0
        for i in nums:
            if i - 1 not in numSet:
                curNum = i + 1
                curLen = 1
                while curNum in numSet:
                    curNum += 1
                    curLen += 1
                ret = max(ret, curLen)
        return ret