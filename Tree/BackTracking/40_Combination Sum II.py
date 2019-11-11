class Solution(object):
    def combinationSum2(self, candidates, target):
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
            if i != 0 and candidate[i] == candidate[i - 1]:
                continue
            if sum(tep) + candidate[i] <= target:
                self.dfs(candidate[i + 1:], tep + [candidate[i]], res, target)
            else:
                return


print Solution().combinationSum2([10, 1, 2, 7, 6, 1, 5], 8)
