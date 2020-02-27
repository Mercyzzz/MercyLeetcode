class Solution(object):
    """
        1. vote algo
        2. Hash
        3. Divide and conquer
    """
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        cnt = 0
        majority = 0
        for num in nums:
            if cnt == 0 or majority == num:
                majority = num
                cnt += 1
            else:
                cnt -= 1
        return majority

print Solution().majorityElement([1,1,1,0,2])