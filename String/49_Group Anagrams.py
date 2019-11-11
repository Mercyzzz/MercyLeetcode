import collections
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        strDict = {}
        for i in strs:
            if tuple(sorted(i)) in strDict:
                strDict[tuple(sorted(i))].append(i)
            else:
                strDict[tuple(sorted(i))] = [i]
        return strDict.values()


print Solution().groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
