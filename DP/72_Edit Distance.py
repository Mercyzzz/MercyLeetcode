class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        dp = [[0 for i in range(len(word2) + 1)] for j in range(len(word1) + 1)]
        dp[0] = [i for i in range(len(word2) + 1)]
        for i in range(len(dp)):
            dp[i][0] = i
        for i in range(1, len(dp)):
            for j in range(1, len(dp[0])):
                same = dp[i - 1][j - 1]
                if word1[i - 1] != word2[j - 1]:
                    same += 1
                dp[i][j] = min(dp[i - 1][j] + 1, dp[i][j - 1] + 1, same)
        return dp[-1][-1]


Solution().minDistance('horse', 'ros')
