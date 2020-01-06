class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        set1 = set()
        for i in nums:
            if i in set1:
                return False
            set1.add(i)
        return True