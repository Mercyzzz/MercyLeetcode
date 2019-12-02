class Solution(object):
    """
        if ordered, we can search binary but time complexity more than two pointers solution
    """
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        nummap = {}
        ret = []
        for i in range(len(numbers)):
            nummap[numbers[i]] = i
        for i in range(len(numbers)):
            idx = nummap.get(target - numbers[i])
            if idx:
                ret.append(i + 1)
                ret.append(idx + 1)
                return ret
print Solution().twoSum([2,7,11,15], 9)