class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        res = []
        self.dfs(candidates, [], res, target)
        return res

    def dfs(self, candidate, tep, res, target):
        if sum(tep) == target:
            res.append(tep)
            return
        for i in range(len(candidate)):
            if sum(tep) + candidate[i] <= target:
                self.dfs(candidate[i:], tep + [candidate[i]], res, target)
            else:
                return


print Solution().combinationSum([8,7,4,3], 11)
