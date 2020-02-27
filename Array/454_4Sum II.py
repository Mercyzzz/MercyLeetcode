class Solution(object):
    def fourSumCount(self, A, B, C, D):
        """
        :type A: List[int]
        :type B: List[int]
        :type C: List[int]
        :type D: List[int]
        :rtype: int
        """
        numDict = {}
        for i in range(len(A)):
            for j in range(len(A)):
                twoSum = A[i] + B[j]
                if twoSum in numDict:
                    numDict[twoSum] += 1
                else:
                    numDict[twoSum] = 1
        res = 0
        for i in range(len(C)):
            for j in range(len(D)):
                twoSum = C[i] + D[j]
                if -twoSum in numDict:
                    res += numDict[-twoSum]
        return res


print Solution().fourSumCount(
[-1,-1],
[-1,1],
[-1,1],
[1,-1])
