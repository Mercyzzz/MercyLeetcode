class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) <= 2:
            return len(nums)
        idx = 2
        for i in range(2, len(nums)):
            if nums[idx - 2] != nums[i]:
                nums[idx] = nums[i]
                idx += 1
        return idx

    def removeDuplicates1(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        for i in range(len(nums)):
            if count < 2 or nums[count - 2] != nums[i]:
                nums[count] = nums[i]
                count += 1
        return count

a = [1,1,1,2,2,3]
print Solution().removeDuplicates(a)
print a