class Solution:
    def twoSum(self, nums, target):
        idxDict = dict()
        idx_list = []
        for idx, num in enumerate(nums):
            if target - num in idxDict:
                idx_list.append([idxDict[target - num], idx])
            idxDict[num] = idx
        return idx_list

    def threeSum(self, num):
        num.sort()
        res = set()
        result = []
        for i in range(len(num) - 2):
            if (i == 0 or num[i] > num[i - 1]) and num[i] <= 0:
                left = i + 1
                result_idx = self.twoSum(num[left:], -num[i])
                for each_idx in result_idx:
                    each_result = tuple([num[i], num[each_idx[0] + (i + 1)], num[each_idx[1] + (i + 1)]])
                    res.add(each_result)
        for value in res:
            result.append(value)
        return result

print Solution().threeSum([-1, 0, 1, 2, -1, -4])