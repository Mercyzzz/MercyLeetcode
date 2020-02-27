class Solution(object):
    def countSmaller(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = [0] * len(nums)
        tep = []
        for i in range(len(nums) - 1, -1, -1):
            left, right = 0, len(tep)
            while left < right:
                mid = (left + right) / 2
                if tep[mid] >= nums[i]:
                    right = mid
                else:
                    left = mid + 1
            res[i] = right
            tep.insert(right, nums[i])
        return res

print Solution().countSmaller([5,2,6,1])