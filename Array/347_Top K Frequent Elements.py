import heapq, queue
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        numDict = {}
        for i in nums:
            if i in numDict:
                numDict[i] += 1
            else:
                numDict[i] = 1
        pq = queue.PriorityQueue()
        for i in numDict:
            pq.put((-numDict[i], i))
        res = []
        for i in range(k):
            res.append(pq.get()[1])
        return res


print Solution().topKFrequent([1, 1, 1, 2, 2, 3], 2)
