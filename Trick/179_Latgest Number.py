class Solution(object):
    """
        Trick : if a = 9, b = 34, and ab = 934 ba = 349,  ab>ba,
                so 'a' sort before 'b'
    """

    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        nums = [str(num) for num in nums]
        nums.sort(cmp=lambda x, y: cmp(y + x, x + y))
        return ''.join(nums).lstrip('0') or '0'

    def qsort(self, nums):
        if len(nums) == 0:
            return []
        left, right = 0, len(nums)
        partition = nums[0]
        while left < right:


print Solution().largestNumber([3, 5, 1, 4, 2])
