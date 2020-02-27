class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        numDict = {}
        for i in nums1:
            if i in numDict:
                numDict[i] += 1
            else:
                numDict[i] = 1
        res = []
        for i in nums2:
            if i in numDict:
                res.append(i)
                numDict[i] -= 1
                if numDict[i] == 0:
                    del(numDict[i])
        return res

print Solution().intersect([1,2,2,1], [2, 2])