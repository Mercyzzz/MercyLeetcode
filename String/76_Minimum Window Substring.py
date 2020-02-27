class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        dT = {}
        for i in t:
            if i not in dT:
                dT[i] = 1
            else:
                dT[i] += 1
        required = len(dT)
        formated = 0
        minLength, minLeft, minRight = float('inf'), 0, 0
        curWin = {}
        left, right = 0, 0
        while right < len(s):
            character = s[right]
            if character in curWin:
                curWin[character] += 1
            else:
                curWin[character] = 1
            if character in dT and curWin[character] == dT[character]:
                formated += 1
            while formated == required and left <= right:
                character = s[left]
                if right - left + 1 < minLength:
                    minLength, minLeft, minRight = right - left + 1, left, right
                curWin[character] -= 1
                if character in dT and curWin[character] < dT[character]:
                    formated -= 1
                left += 1
            right += 1
        return "" if minLength == float('inf') else s[minLeft:minRight + 1]

print Solution().minWindow('aaaaa', 'aa')
