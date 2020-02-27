class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        total, curSum, start = 0, 0, 0
        for i in range(len(gas)):
            total += gas[i] - cost[i]
            curSum += gas[i] - cost[i]
            if curSum < 0:
                start = i + 1
                curSum = 0
        return -1 if total < 0 else start

print Solution().canCompleteCircuit([1, 2, 3, 4, 5], [3, 4, 5, 1, 2])
