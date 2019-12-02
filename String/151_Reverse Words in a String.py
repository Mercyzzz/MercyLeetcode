class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        s.lstrip('')
        reversed(s)
        s.lstrip()
        insertIdx = 0
        startIdx, endIdx = 0, 0
        for i in range(len(s)):
            if i != '':
                endIdx += 1
            else:
                str = s[startIdx:endIdx + 1]
                strIdx = len(str) - 1
                for j in (strIdx, -1, -1):
                    s[insertIdx] = strIdx[j]
                    insertIdx += 1
                