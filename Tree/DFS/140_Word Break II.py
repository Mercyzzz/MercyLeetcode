import copy
class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        sDict ={}
        return self.dfs(s, wordDict, sDict)

    def dfs(self, s, wordDict, m):
        if s in m:
            return m[s]
        if not s:
            return [""]
        res = []
        for word in wordDict:
            if s[0:len(word)] != word:
                continue
            rem = self.dfs(s[len(word):], wordDict, m)
            for str in rem:
                if str == "":
                    res.append(word)
                else:
                    res.append(word + " " + str)
        m[s] = res
        print m
        return res

print Solution().wordBreak('aaaaaaaab', ["b", "a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"])